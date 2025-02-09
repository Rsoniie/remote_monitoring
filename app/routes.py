from flask import render_template, request, jsonify
from app import app, mongo
from app.utils import generate_random_user, genrate_random_health_data
from datetime import datetime
# import random


@app.route("/")
def home():
    return render_template("index.html", title="Home")



@app.route("/add_user", methods=["POST"])
def add_user():

    try:
        if not request.is_json:
            return jsonify({"error": "Content-Type must be 'application/json'"}), 415
        # data = generate_random_user()
        data = request.get_json(silent=True)
        username = data.get("username")
        password = data.get("password")
        parent_email = data.get("email")


        if not username or not password:
            return jsonify({"error": "Username and password are required!"}), 400
        
        user_data = {
            "username": username,
            "email": parent_email,
            "password": password,
            "health_data": [],
            "created_at": datetime.utcnow()
        }
        chk = mongo.cx['remote'].users.find_one({"username": username})
        if chk:
            return jsonify({"message" : "Existing Username"}), 400
        mongo.cx['remote'].users.insert_one(user_data) 
        return jsonify({"message": "User added successfully!"})
    

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500




@app.route("/add_to_all", methods=["POST"])
def add_to_all():
    try:
        users = mongo.cx['remote'].users.find({})
        users_list = []
        for user in users:

            health_data = genrate_random_health_data()

            mongo.cx['remote'].users.update_one(
                {"_id": user["_id"]},
                {"$push": {"health_data": { "$each" : [health_data] , "$slice": -10}}}
            )

            user["_id"] = str(user["_id"])


            users_list.append(user)
        return jsonify({"message": f"All user updated successfully.", "users_list": users_list}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500



@app.route("/history/<username>", methods=["GET"])
def history(username):
    try:
        # user = mongo.db.users.find_one({"username": username})  # for compass

        user = mongo.cx['remote'].users.find_one({"username": username})

        if not user:
            return jsonify({"error": f"User not found: {str(e)}"}), 404
        history_data = []

        history_data = user["health_data"]
        return jsonify({"history": history_data})
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve history: {str(e)}"}), 500
    



@app.route("/login", methods=["POST"])
def login():
        
        try:
            if not request.is_json:
                return jsonify({"error": "Content-Type must be 'application/json'"}), 415

            data = request.get_json(silent=True)
            if data is None:
                return jsonify({"error": "Invalid or empty JSON payload"}), 400

            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return jsonify({"error": "Username and password are required!"}), 400
        
            user = mongo.cx['remote'].users.find_one({"username": username})
            if not user:
                return jsonify({"error": "Invalid username or password"}), 401
        
            if user["password"] != password:
                return jsonify({"error": "Wrong Password"}), 401
        
            return jsonify({"message": f"Welcome back, {username}!", "username": username}), 200
        except Exception as e:
            return jsonify({"error": f"Failed to retrieve history: {str(e)}"}), 500

        

@app.route("/show/<username>", methods = ["GET"])
def show(username):
    try:

        user = mongo.cx['remote'].users.find_one({"username": username})
        current_data = user["health_data"][-1]
        return jsonify({"current_data": current_data})




    except Exception as e:
        return jsonify({"error": f"Failed to retrieve recent_data : {str(e)}"}), 500



