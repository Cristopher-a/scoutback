from flask import Flask, request, jsonify
import cloudinary
import cloudinary.uploader
from supabase import create_client, Client

SUPABASE_URL = "https://rhttqmtzcmwilzshnxwq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJodHRxbXR6Y213aWx6c2hueHdxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM1OTUwOTAsImV4cCI6MjA3OTE3MTA5MH0.8dYvM8CBEdqiF9ZZhaYRKhtOin_wYGf4JYrmTTIsX74"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

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
    data= {
        "region": region,
        "traction_type": traction_type,
        "specialty": specialty,
        "team_number": team_number,
        "battery_number": battery_number,
        "robot_image": robot_url,
        "strategy_image": strategy_url,
        "strategy_comment": strategy_comment
    }

    response = supabase.table("pits").insert(data).execute()
    # Process the data as needed
    return jsonify({"message": "Pits data received", "data": body})