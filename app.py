from flask import Flask, jsonify, request, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)


# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # 👉 replace with env var in real apps
jwt = JWTManager(app)

# Sample Data
members = {
    1: {"name": "Taylor", "age": 25, "membership": "Gold"},
    2: {"name": "Travis", "age": 30, "membership": "Silver"},
    3: {"name": "Harry", "age": 28, "membership": "Platinum"},
}

workouts = [
    {"id": 1, "name": "Cardio Blast", "duration": "30 mins"},
    {"id": 2, "name": "Strength Training", "duration": "45 mins"},
    {"id": 3, "name": "Yoga Flex", "duration": "60 mins"},
]

trainers = [
    {"id": 1, "name": "Coach Mike", "specialty": "Strength"},
    {"id": 2, "name": "Coach Sarah", "specialty": "Yoga"},
]

classes = [
    {"id": 1, "name": "Morning Yoga", "time": "7 AM"},
    {"id": 2, "name": "HIIT", "time": "6 PM"},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/members")
def get_members():
    return jsonify(members)

@app.route("/membership/<int:member_id>")
def get_member(member_id):
    if member_id in members:
        return jsonify(members[member_id])
    return jsonify({"error": "Member not found"}), 404

@app.route("/workouts")
def get_workouts():
    return jsonify(workouts)

@app.route("/trainers")
def get_trainers():
    return jsonify(trainers)

@app.route("/classes")
def get_classes():
    return jsonify(classes)

@app.route("/bmi")
def calculate_bmi():
    try:
        weight = float(request.args.get("weight"))
        height = float(request.args.get("height"))
        bmi = round(weight / (height * height), 2)
        return jsonify({"BMI": bmi})
    except:
        return jsonify({"error": "Invalid input"}), 400

@app.route("/login", methods=["POST"])
def login():
    """
    Login with username + password (hardcoded for demo).
    Returns JWT token.
    """
    username = request.json.get("username")
    password = request.json.get("password")

    # Demo credentials (replace with DB in real app)
    if username == "admin" and password == "admin":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/protected")
@jwt_required()
def protected():
    """
    Protected route – requires valid JWT.
    """
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello, {current_user}. You are authorized!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
