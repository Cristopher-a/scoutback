from flask import Flask, request, jsonify
import cloudinary
import cloudinary.uploader

# Configura Cloudinary antes de usar
cloudinary.config(
    cloud_name="djlskhtyf",
    api_key="596625527778167",
    api_secret="zTTEjWP4apxgFF8a-kYNRTzT_XY"
)
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/pits', methods=['POST'])
def pits():
    body = request.get_json()
    region= body.get("region")
    traction_type= body.get("traction_type")
    specialty= body.get("specialty")
    team_number= body.get("team_number")
    battery_number= body.get("battery_number")
    robot_image= body.get("robot_image")
    strategy_image= body.get("strategy_image")
    strategy_comment= body.get("strategy_comment")
    robot_url = None
    strategy_url = None
    if robot_image:
        robot_url = cloudinary.uploader.upload(robot_image).get("secure_url")

    if strategy_image:
        strategy_url = cloudinary.uploader.upload(strategy_image).get("secure_url")

    # Process the data as needed
    return jsonify({"message": "Pits data received", "data": body})