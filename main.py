from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration (Using SQLite)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Define a model for storing hotel room status
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # "occupied" or "unoccupied"

# Create the database tables (Run this once)
with app.app_context():
    db.create_all()

# Route to render the HTML page
@app.route("/")
def index():
    rooms = Room.query.all()
    return render_template("index.html", rooms=rooms)

# Route to upload hotel reports (inhouse and departure)
@app.route("/upload", methods=["POST"])
def upload_reports():
    inhouse_rooms = request.form.get("inhouse").split(",")  # Simulating CSV input
    departure_rooms = request.form.get("departure").split(",")

    # Reset all rooms to "unoccupied" before processing
    Room.query.delete()

    # Mark inhouse rooms as occupied
    for room in inhouse_rooms:
        db.session.add(Room(number=room.strip(), status="occupied"))

    # Commit changes
    db.session.commit()

    # Count unoccupied rooms
    total_rooms = 100  # Adjust this as needed
    occupied_count = Room.query.count()
    unoccupied_count = total_rooms - occupied_count

    return {"unoccupied_rooms": unoccupied_count}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
