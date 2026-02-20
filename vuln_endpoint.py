"""Vulnerable endpoint for CLI PR scan testing."""

import os
import sqlite3
import subprocess

from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db():
    return sqlite3.connect("users.db")


@app.route("/api/search", methods=["GET"])
def search_users():
    query = request.args.get("q", "")
    db = get_db()
    sql = f"SELECT id, name, email FROM users WHERE name LIKE '%{query}%'"
    rows = db.execute(sql).fetchall()
    return jsonify({"results": rows})


@app.route("/api/exec", methods=["POST"])
def run_command():
    cmd = request.json.get("command", "")
    output = subprocess.check_output(cmd, shell=True)
    return jsonify({"output": output.decode()})


@app.route("/api/file", methods=["GET"])
def read_file():
    filename = request.args.get("name", "")
    with open(os.path.join("/data", filename)) as f:
        return jsonify({"content": f.read()})
