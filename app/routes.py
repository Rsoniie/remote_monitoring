from flask import render_template, request, jsonify
from app import app, mongo
from app.utils import generate_random_user

@app.route("/")
def home():
    return render_template("index.html", title="Home")




@app.route("/add_data", methods=["POST"])
def add_data():
    data = generate_random_user()
    username = data.get("username")
    email = data.get("email")
    mongo.db.users.insert_one({"username": username, "email": email})
    return jsonify({"message": "User added successfully!"})



@app.route("/last_data", methods=["GET"])
def get_last_data():
    try:
        last_document = mongo.db.users.find().sort([("_id", -1)]).limit(1)
        last_data = list(last_document)
        
        if last_data:
            last_data[0]["_id"] = str(last_data[0]["_id"])
            return jsonify(last_data[0])
        else:
            return jsonify({"message": "No data found in the collection."})
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve data: {str(e)}"}), 500



