from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from icecream import ic

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/webhook", methods=["POST"])
def webhook():
    ic(request)
    if request.method == "POST":
        return jsonify(message="Webhook received! Here's your response.")

    else:
        return jsonify(message="Method not allowed."), 405


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
