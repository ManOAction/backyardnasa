from flask import Flask, request, jsonify, render_template, render_template_string
from flask_cors import CORS
from icecream import ic

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/button_response", methods=["GET"])
def webhook():
    ic(request)
    message = "You pressed the button!"
    return render_template_string("<span>{{ message }}</span>", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
