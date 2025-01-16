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
        email = data.get("email")


        if not username or not password:
            return jsonify({"error": "Username and password are required!"}), 400
        
        user_data = {
            "username": username,
            "email": email,
            "password": password,
            "health_data": [],
            "created_at": datetime.utcnow()
        }
        mongo.cx['remote'].users.insert_one(user_data) 
        return jsonify({"message": "User added successfully!"})
    

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500




@app.route("/add_data/<username>", methods=["POST"])
def add_data(username):
    try:
        health_data = genrate_random_health_data()
        # user = mongo.db.users.find_one({"username":username}) # for compass
        user = mongo.cx['remote'].users.find_one({"username":username}) 
        if not user:
            return jsonify({"error": f"User with username '{username}' not found."}), 404

        # mongo.db.users.update_one(
        #     {"username": username},
        #     {"$push": {"health_data": health_data}}          # This is for compass
        # )

        mongo.cx['remote'].users.update_one(
            {"username": username},
            {"$push": {"health_data" : health_data}}   # This is for mongodb atlas
        )
        
        return jsonify({"message": f"Health_Data is added successfully for user '{username}'",
        "Health Data": health_data}), 200

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
                {"$push": {"health_data": health_data}}
            )
        return jsonify({"message": f"All user updated successfully."}), 200
    
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

        




