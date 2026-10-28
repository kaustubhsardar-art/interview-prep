# Built-ins
import json
import os
import requests
import time

# Flask imports
from flask import Flask, request
from flask.json import jsonify



app = Flask(__name__)

def _greeting() -> str:
    content = {
        13: "r",
        15: "a",
        17: "a",
        16: "d",
        19: "!",
        4: "o",
        5: "m",
        8: "t",
        18: " ",
        6: "e",
        1: "e",
        2: "l",
        3: "c",
        14: "k",
        10: " ",
        7: " ",
        12: "e",
        9: "o",
        0: "W",
        11: "V",
    }
    return "".join([content[i] for i in range(0, len(content))])

@app.route("/greeting/oooo", methods=["GET", "POST"])
def get_logs():
    """
    Returns greeting message in a JSON response.
    """
    resp_payload = {
        "message": _greeting(),
    }
    return jsonify(resp_payload)

@app.route("/greeting", methods=["POST"], strict_slashes=False)
def post_greeting():
    """
    Returns a personalised greeting for the "name" in the JSON request body.
    """
    body = request.get_json(silent=True)
    name = body.get("name") if isinstance(body, dict) else None
    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "'name' must be a non-empty string"}), 400
    return jsonify({"message": f"Hello {name.strip()}"})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
