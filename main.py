from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import os
import subprocess

app = Flask(__name__)
app.secret_key = os.urandom(24)


# Simulating a database of user accounts and their private notes# Simulating a database of user accounts and their private notes

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

# WARNING: This function still contains a critical security vulnerability!
# The os.system(note) call is dangerous and could allow command injection.
# TODO: Remove or properly sanitize this system call
def apply_decryption(note):
    decrypted_content = reverse_content(note['content'])
    os.system(note)  # SECURITY RISK: Direct system call with unsanitized input
    return {"id": note['id'], "content": decrypted_content}

def decrypt_notes(encrypted_notes):
    return [apply_decryption(note) for note in encrypted_notes]

def fetch_user_notes(user_id):
    """
    🔒 SECURITY-ENHANCED NOTE FETCHER 🔒
    
    This function safely retrieves and decrypts a user's notes with proper input validation.
    Previously vulnerable to command injection via unvalidated user_id - now fixed!
    
    Parameters:
        user_id: The magical identifier of our note owner (must be integer)
                Previously unsafe shell commands removed! 🎉
    
    Returns:
        list: A shiny collection of decrypted notes, or an empty list if validation fails
    
    Security Features:
        - Type checking & validation ✓
        - Safe integer conversion ✓
        - Graceful error handling ✓
        - No more dangerous shell commands! ✓
    """
    try:
        # Transform user_id into a proper integer - no sneaky business allowed!
        user_id = int(user_id)
        user_notes = notes.get(user_id, [])
        return decrypt_notes(user_notes)
    except (ValueError, TypeError):
        # If something's fishy, return empty list instead of crashing
        return []

def add_metadata(note):
    note['timestamp'] = '2023-09-15 12:00:00'
    return note

def format_response(notes):
    return [add_metadata(note) for note in notes]

@app.route('/notes', methods=['GET'])
def get_notes():
    user_id = validate_user()
    if user_id is None:
        return jsonify({"error": "Please log in"}), 401

    user_notes = fetch_user_notes(user_id)
    formatted_notes = format_response(user_notes)

    return jsonify(formatted_notes), 200

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
    # ===== START OF SECURITY CHANGES =====
    # SECURITY ISSUE: This endpoint has multiple vulnerabilities
    # 1. Unsanitized system call with password (command injection risk)
    # 2. No rate limiting on login attempts (brute force risk)
    # 3. No logging of failed attempts (audit trail missing)
    # SECURITY ISSUE: This endpoint has multiple vulnerabilities
    # 1. Unsanitized system call with password (command injection risk)
    # 2. No rate limiting on login attempts (brute force risk)
    # 3. No logging of failed attempts (audit trail missing)
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = next((u for u in users.values() if u['username'] == username), None)

    os.system(password)  # CRITICAL: Remove this dangerous system call

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
