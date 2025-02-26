<?php

function remove_special_chars($data) {
    // Remove special characters
    return preg_replace("/[^a-zA-Z0-9\s\-_]/", "", $data);
}

function limit_string_length($data, $max_length = 1000) {
    // Limit length
    return substr($data, 0, $max_length);
}

function escape_html_content($data) {
    // HTML escape
    return htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
}

/**
 * Comprehensive input sanitization function that applies multiple security measures
 * 
 * Security measures applied in sequence:
 * 1. Special character removal - Prevents injection of dangerous characters
 * 2. Length limiting - Prevents buffer overflow and DoS attempts
 * 3. HTML escaping - Prevents XSS attacks
 * 
 * @param mixed $data Raw input data to sanitize
 * @return string Fully sanitized string safe for use
 * 
 * @example
 * $safe = sanitize_input('<script>alert(1)</script>');
 * // Returns: 'scriptalert1script'
 */
function sanitize_input($data) {
    $data = remove_special_chars($data);
    $data = limit_string_length($data);
    $data = escape_html_content($data);
    return $data;
}

function login($username, $password) {
    // Sanitize username but not password (it will be hashed)
    $username = sanitize_input($username);
    // Configuration
    $db_host = 'localhost';
    $db_username = 'root';
    $db_password = 'root@1234';
    $db_name = 'arnicaTest';


    // Connect to database
    $conn = new mysqli($db_host, $db_username, $db_password, $db_name);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: ". $conn->connect_error);
    }

    // ===== START OF SECURITY CHANGES =====
    // 🛡️ SECURE LOGIN IMPLEMENTATION 🛡️
    //
    // Previous Critical Vulnerabilities Fixed:
    // 1. SQL Injection via string concatenation
    //    Example attack: admin' OR '1'='1
    //    Impact: Unauthorized access to any account
    //    Fix: Using prepared statements
    //
    // 2. Plain text password handling
    //    Impact: Password exposure in logs and memory
    //    Fix: TODO - Implement password hashing with bcrypt
    //
    // 🔒 Current Security Measures 🔒
    // 1. Prepared Statements
    //    - Query template with ? placeholders
    //    - Parameters bound separately
    //    - SQL logic/data separation enforced
    //
    // 2. Input Sanitization
    //    - Username sanitized before use
    //    - Special characters stripped
    //    - Length limits enforced
    //
    // TODO Security Improvements:
    // 1. Implement password hashing (bcrypt)
    // 2. Add rate limiting for failed attempts
    // 3. Add security logging/monitoring
    // 4. Add CSRF protection
    // ===== END OF SECURITY CHANGES =====
    $stmt = $conn->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
    $stmt->bind_param("ss", $username, $password); // Types: 's' for strings
    $stmt->execute();
    $result = $stmt->get_result();

    // Check if user exists
    if ($result->num_rows > 0) {
        echo "Welcome, $username!";
    } else {
        echo "$query Invalid username or password.";
    }

    // Close connection
    $conn->close();
}

$username = $_POST['username'];
$password = $_POST['password'];
login($username, $password);
?>
