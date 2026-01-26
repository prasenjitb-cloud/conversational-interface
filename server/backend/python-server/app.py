import flask
import flask_cors

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if flask.request.method == "GET":
        message = flask.request.args.get("message", "")
    else:
        data = flask.request.get_json(silent=True) or {}
        message = data.get("message", "")

    return flask.jsonify({
        "reply": f"{message}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
