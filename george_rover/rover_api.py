from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        print("Data received from Webhook is: ", request.json)
        # Create a response message
        return jsonify(message="Webhook received! Here's your response.")


app.run(host="0.0.0.0", port=8000)
