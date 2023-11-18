from flask import Flask, request, jsonify, render_template, render_template_string
from flask_cors import CORS
from icecream import ic

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/button_response1", methods=["GET"])
def response_1():
    ic(request)
    message = "You pressed button number one!"
    return render_template_string("<span>{{ message }}</span>", message=message)


@app.route("/button_response2", methods=["GET"])
def response_2():
    ic(request)
    message = "You pressed button number two!"
    return render_template_string("<span>{{ message }}</span>", message=message)


@app.route("/button_response3", methods=["GET"])
def response_3():
    ic(request)
    message = "You pressed button number three!"
    return render_template_string("<span>{{ message }}</span>", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
