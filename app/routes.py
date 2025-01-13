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
        data = generate_random_user()
        # username = data.get("username")
        # email = data.get("email")
        # health_data = data.get("health_data");
        # mongo.db.users.insert_one({"username": username, "email": email, "health_data": health_data, "created_at": datetime.utcnow()})
        mongo.db.users.insert_one(data)
        return jsonify({"message": "User added successfully!"})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500




@app.route("/add_data/<username>", methods=["POST"])
def add_data(username):
    try:
        health_data = genrate_random_health_data()
        user = mongo.db.users.find_one({"username":username})
        if not user:
            return jsonify({"error": f"User with username '{username}' not found."}), 404

        mongo.db.users.update_one(
            {"username": username},
            {"$push": {"health_data": health_data}}
        )
        
        return jsonify({"message": f"Health_Data is added successfully for user '{username}'",
        "Health Data": health_data}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500









@app.route("/history/<username>", methods=["GET"])
def history(username):
    try:
        user = mongo.db.users.find_one({"username": username})

        if not user:
            return jsonify({"error": f"User not found: {str(e)}"}), 404
        history_data = []

        history_data = user["health_data"]
        return jsonify({"history": history_data})
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve history: {str(e)}"}), 500