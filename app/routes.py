from flask import render_template, request, jsonify
from app import app, mongo
from app.utils import generate_random_user
from datetime import datetime

@app.route("/")
def home():
    return render_template("index.html", title="Home")



@app.route("/add_data", methods=["POST"])
def add_data():
    data = generate_random_user()
    username = data.get("username")
    email = data.get("email")
    mongo.db.users.insert_one({"username": username, "email": email, "created_at": datetime.utcnow()})
    return jsonify({"message": "User added successfully!"})


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