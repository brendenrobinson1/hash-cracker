from flask import Flask, render_template, request, jsonify
import os
from threading import Thread
from hashcracker_core import crack_hash, SUPPORTED_ALGORITHMS

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

status = {
    "running": False,
    "progress": 0,
    "attempts": 0,
    "total": 0,
    "found": False,
    "password": None,
    "time": 0,
    "speed": 0
}


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


def run_cracker(target_hash, wordlist_file, algorithm, rules):
    global status

    password = crack_hash(
        target_hash,
        algorithm,
        wordlist_file,
        rules=rules,
        status=status
    )

    status["running"] = False
    status["progress"] = 100

    if password:
        status["found"] = True
        status["password"] = password
    else:
        status["found"] = False
        status["password"] = None


@app.route("/start", methods=["POST"])
def start():
    global status

    if status["running"]:
        return jsonify({"error": "Cracker is already running."}), 400

    target_hash = request.form.get("hash", "").strip()
    algorithm = request.form.get("type", "").lower()
    rules = request.form.get("rules", "light").lower()
    uploaded_file = request.files.get("wordlist_file")

    if not target_hash:
        return jsonify({"error": "Please enter a hash."}), 400

    if algorithm not in SUPPORTED_ALGORITHMS:
        return jsonify({"error": "Unsupported hash type."}), 400

    if rules not in ["none", "light", "medium", "heavy"]:
        return jsonify({"error": "Unsupported rule strength."}), 400

    if not uploaded_file or not uploaded_file.filename:
        return jsonify({"error": "Please upload a wordlist file."}), 400

    wordlist_file = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
    uploaded_file.save(wordlist_file)

    status.update({
        "running": True,
        "progress": 0,
        "attempts": 0,
        "total": 0,
        "found": False,
        "password": None,
        "time": 0,
        "speed": 0
    })

    thread = Thread(
        target=run_cracker,
        args=(target_hash, wordlist_file, algorithm, rules)
    )

    thread.daemon = True
    thread.start()

    return jsonify({"message": "Cracking started."})


@app.route("/status")
def get_status():
    return jsonify(status)


if __name__ == "__main__":
    app.run(debug=True)