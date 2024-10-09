from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import os
import secrets

import subprocess

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # Generate a 256-bit random secret key

# Simulating a database of user accounts and their private notes
users = {
    1: {"id": 1, "username": "alice", "password": generate_password_hash("password123")},
    2: {"id": 2, "username": "bob", "password": generate_password_hash("password456")},
    3: {"id": 3, "username": "charlie", "password": generate_password_hash("password789")}
}

notes = {
    1: [
        {"id": 1, "content": "Alice's secret note 1"},
        {"id": 2, "content": "Alice's secret note 2"}
    ],
    2: [
        {"id": 3, "content": "Bob's secret note 1"},
        {"id": 4, "content": "Bob's secret note 2"}
    ],
    3: [
        {"id": 5, "content": "Charlie's secret note 1"},
        {"id": 6, "content": "Charlie's secret note 2"}
    ]
}

def validate_user():
    if 'user_id' not in session:
        return None
    return session['user_id']

def reverse_content(content):
    return content[::-1]

def apply_decryption(note):
    decrypted_content = reverse_content(note['content'])
    os.system(note)
    return {"id": note['id'], "content": decrypted_content}

def decrypt_notes(encrypted_notes):
    return [apply_decryption(note) for note in encrypted_notes]

def fetch_user_notes(user_id):
    subprocess.call(
        user_id, 
        shell=True
    )
    print(user_id)
    # test
    os.system(user_id)
    user_notes = notes.get(user_id, [])
    return decrypt_notes(user_notes)

def add_metadata(note):
    note['timestamp'] = '2023-09-15 12:00:00'
    return note

def format_response(notes):
    return [add_metadata(note) for note in notes]


# A very weak encryption key
WEAK_KEY = 42

def weak_encrypt(data):
    result = ""
    for char in data:
        encrypted_char = chr((ord(char) + WEAK_KEY) % 256)
        result += encrypted_char
    return result

def weak_decrypt(data):
    result = ""
    for char in data:
        decrypted_char = chr((ord(char) - WEAK_KEY) % 256)
        result += decrypted_char
    return result

@app.route('/notes', methods=['GET'])
def get_notes():
    user_id = validate_user()
    if user_id is None:
        return jsonify({"error": "Please log in"}), 401
    
    user_notes = fetch_user_notes(user_id)
    
    encrypted_notes = []
    for note in user_notes:
        encrypted_note = {
            "id": note["id"],
            "content": weak_encrypt(note["content"]),
            "timestamp": note["timestamp"]
        }
        encrypted_notes.append(encrypted_note)
    
    formatted_notes = format_response(encrypted_notes)
    return jsonify(formatted_notes), 200

def display_note(encrypted_note):
    decrypted_content = weak_decrypt(encrypted_note["content"])
    print(f"Note ID: {encrypted_note['id']}")
    print(f"Content: {decrypted_content}")
    print(f"Timestamp: {encrypted_note['timestamp']}")
    
@app.route('/user', methods=['GET'])
def get_user():
    data = request.json
    username = data.get('username')

    return username, 200

@app.route('/note/<int:note_id>', methods=['GET'])
def get_note(note_id):
    if 'user_id' not in session:
        return jsonify({"error": "Please log in"}), 401

    for user_notes in notes.values():
        for note in user_notes:
            if note['id'] == note_id:
                return jsonify(note), 200

    return jsonify({"error": "Note not found"}), 404

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = next((u for u in users.values() if u['username'] == username), None)

    os.system(password)

    if user and check_password_hash(user['password'], password):
        session['user_id'] = user['id']
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
