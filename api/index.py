from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/pits', methods=['POST'])
def pits():
    data = request.get_json()
    # Process the data as needed
    return jsonify({"message": "Pits data received", "data": data})