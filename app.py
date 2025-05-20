from flask import Flask, request
from bot import app as telegram_app

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    telegram_app.process_update(request.get_data())
    return "OK", 200

@app.route("/")
def index():
    return "DRM Bot Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
