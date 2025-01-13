from flask import render_template, request, jsonify
from app import app, mongo
from app.utils import generate_random_user, genrate_random_health_data
from datetime import datetime
import random


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
        
        return jsonify({"message": f"Data added successfully for user '{username}'."}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500






@app.route("/latest_data", methods=["GET"])
def get_latest_data():
    try:
        # last_document = mongo.db.users.find().sort([("_id", -1)]).limit(1)
        latest_document = mongo.db.users.find().sort([("created_at", -1)]).limit(1)
        latest_data = list(latest_document)
        
        if latest_data:
            latest_data[0]["_id"] = str(latest_data[0]["_id"])
            return jsonify(latest_data[0])
        else:
            return jsonify({"message": "No data found in the collection."})
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve data: {str(e)}"}), 500




@app.route("/history", methods=["GET"])
def history():
    try:
        documents = mongo.db.users.find().sort([("created_at", -1)]).limit(10)
        history_data = []
        for doc in documents:
            doc["_id"] = str(doc["_id"])
            history_data.append(doc)
        return jsonify({"history": history_data})
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve history: {str(e)}"}), 500