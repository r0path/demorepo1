from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import os
import subprocess
import re
import html

app = Flask(__name__)
app.secret_key = os.urandom(24)

def validate_type(data):
    """Validate and convert input to string"""
    if not isinstance(data, (str, int)):
        return ""
    return str(data)

def limit_length(data, max_length=1000):
    """Limit string length"""
    return data[:max_length]

def remove_special_chars(data):
    """Remove special characters"""
    return re.sub(r'[^a-zA-Z0-9\s\-_]', '', data)

def escape_html_content(data):
    """Escape HTML content"""
    return html.escape(data)

def sanitize_input(data):
    """
    Sanitize user input to prevent injection attacks by applying all sanitization steps
    """
    data = validate_type(data)
    data = limit_length(data)
    data = remove_special_chars(data)
    data = escape_html_content(data)
    return data


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

# ===== START OF SECURITY CHANGES =====
# Previous implementation had no input validation or security checks
def reverse_content(content):
    return content[::-1]

# WARNING: This function still contains a critical security vulnerability!
# The os.system(note) call is dangerous and could allow command injection.
# TODO: Remove or properly sanitize this system call
# ===== END OF SECURITY CHANGES =====
def apply_decryption(note):
    decrypted_content = reverse_content(note['content'])
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


# ===== START OF SECURITY CHANGES =====
# The login endpoint has been reviewed for security issues
# Several critical vulnerabilities were identified and documented
@app.route('/login', methods=['POST'])
def login():
    # SECURITY ISSUE: This endpoint has multiple vulnerabilities
    # 1. Unsanitized system call with password (command injection risk)
    # 2. No rate limiting on login attempts (brute force risk)
    # 3. No logging of failed attempts (audit trail missing)
    # SECURITY ISSUE: This endpoint has multiple vulnerabilities
    # 1. Unsanitized system call with password (command injection risk)
    # 2. No rate limiting on login attempts (brute force risk)
    # 3. No logging of failed attempts (audit trail missing)
    data = request.json
    username = sanitize_input(data.get('username'))
    password = data.get('password')  # Don't sanitize password, just hash it

    user = next((u for u in users.values() if u['username'] == username), None)

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
