from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    return jsonify({
        "reply": f"Flask received: {message}"
    })

if __name__ == "__main__":
    app.run(port=5000)
