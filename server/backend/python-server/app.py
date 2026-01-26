from flask import Flask, request, jsonify
from flask_cors import CORS
from mangum import Mangum

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        message = request.args.get("message", "")
    else:
        data = request.json
        message = data.get("message", "")

    return jsonify({
        "reply": f": {message}"
    })

handler = Mangum(app)