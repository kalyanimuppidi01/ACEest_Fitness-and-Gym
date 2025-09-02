from flask import Flask, jsonify, request, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import threading
import os

if not os.environ.get("DOCKER_ENV"):
    import tkinter as tk
    from tkinter import messagebox

# -------------------- Flask Web App -------------------- #
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
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
    except Exception:
        return jsonify({"error": "Invalid input"}), 400

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if username == "admin" and password == "admin":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/protected")
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello, {current_user}. You are authorized!"})

# -------------------- Tkinter GUI App -------------------- #
class FitnessTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("ACEst Fitness and Gym")

        self.workouts = []

        self.workout_label = tk.Label(master, text="Workout:")
        self.workout_label.grid(row=0, column=0, padx=5, pady=5)
        self.workout_entry = tk.Entry(master)
        self.workout_entry.grid(row=0, column=1, padx=5, pady=5)

        self.duration_label = tk.Label(master, text="Duration (minutes):")
        self.duration_label.grid(row=1, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(master)
        self.duration_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Workout", command=self.add_workout)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(master, text="View Workouts", command=self.view_workouts)
        self.view_button.grid(row=3, column=0, columnspan=2, pady=5)

    def add_workout(self):
        workout = self.workout_entry.get()
        duration_str = self.duration_entry.get()

        if not workout or not duration_str:
            messagebox.showerror("Error", "Please enter both workout and duration.")
            return

        try:
            duration = int(duration_str)
            self.workouts.append({"workout": workout, "duration": duration})
            messagebox.showinfo("Success", f"'{workout}' added successfully!")
            self.workout_entry.delete(0, tk.END)
            self.duration_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Duration must be a number.")

    def view_workouts(self):
        if not self.workouts:
            messagebox.showinfo("Workouts", "No workouts logged yet.")
            return

        workout_list = "Logged Workouts:\n"
        for i, entry in enumerate(self.workouts):
            workout_list += f"{i+1}. {entry['workout']} - {entry['duration']} minutes\n"
        messagebox.showinfo("Workouts", workout_list)

# -------------------- Run Both -------------------- #
# -------------------- Run Both -------------------- #
def run_flask():
    # Disable reloader to avoid signal issues in thread
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)

def run_tkinter():
    root = tk.Tk()
    gui_app = FitnessTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    if os.environ.get("DOCKER_ENV"):
        # In Docker: run only Flask
        run_flask()
    else:
        # Locally: run Flask + Tkinter together
        threading.Thread(target=run_flask, daemon=True).start()
        run_tkinter()

