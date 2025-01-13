from flask import render_template, request, jsonify
from app import app, mongo

@app.route("/")
def home():
    return render_template("index.html", title="Home")


@app.route("/add_data", methods=["POST"])
def add_data():
    
    data = request.json
    username = data.get("username")
    email = data.get("email")
    mongo.db.users.insert_one({"username": username, "email": email})
    return jsonify({"message": "User added successfully!"})