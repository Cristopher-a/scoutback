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

@app.route('/match', methods=['POST'])
def match():
    body = request.json()
    team_number= body.get("team_number")
    match_number= body.get("match_number")
    regional= body.get("regional")
    check_inicio= body.get("check_inicio")
    count_motiv= body.get("count_mottif")
    count_in_cage_auto= body.get("count_in_cage_auto")
    count_out_cage_auto= body.get("count_out_cage_auto")
    count_in_cage_teleop= body.get("count_in_cage_teleop")
    count_out_cage_teleop= body.get("count_out_cage_teleop")
    count_rp= body.get("count_rp")
    check_scoring= body.get("check_scoring")
    count_in_cage_endgame= body.get("count_in_cage_endgame")    
    count_out_cage_endgame= body.get("count_out_cage_endgame")
    check_full_park= body.get("check_full_park")
    check_partial_park= body.get("check_partial_park")
    check_high= body.get("check_high")
    robot_rating= body.get("robot_rating")
    comment_robot= body.get("comment_robot")
    driver_rating= body.get("driver_rating")
    comment_driver= body.get("comment_driver")
    general_rating= body.get("general_rating")
    comment_general= body.get("comment_general")
    data  ={
        "team_number": team_number,
        "match_number": match_number,
        "regional": regional,

        "check_inicio": check_inicio*3,
        "count_motiv": count_motiv*2,
        "count_in_cage_auto": count_in_cage_auto*3,
        "count_out_cage_auto": count_out_cage_auto*1,

        "count_in_cage_teleop": count_in_cage_teleop*3,
        "count_out_cage_teleop": count_out_cage_teleop*1,
        "count_rp": count_rp,

        "check_scoring": check_scoring,
        "count_in_cage_endgame": count_in_cage_endgame*3,
        "count_out_cage_endgame": count_out_cage_endgame*1,
        "check_full_park": 10 if check_full_park  =="Sí" else 0,
        "check_partial_park": 5 if check_partial_park  =="Sí" else 0,
        "check_high": 10 if check_high == "Sí" else 0,

        "robot_rating": robot_rating,
        "comment_robot": comment_robot,
        "driver_rating": driver_rating,
        "comment_driver": comment_driver,
        "general_rating": general_rating,
        "comment_general": comment_general
    }

    response = supabase.table("matches").insert(data).execute()
    return jsonify(response), 200