<?php

function sanitize_input($data) {
    // Remove special characters
    $data = preg_replace("/[^a-zA-Z0-9\s\-_]/", "", $data);
    
    // Limit length
    $data = substr($data, 0, 1000);
    
    // HTML escape
    $data = htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
    
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
    // Previous vulnerability:
    // The old code was vulnerable to SQL injection attacks like:
    // Username: admin
    // Password: ' OR '1'='1
    //
    // 🔒 Security Enhancement 🔒
    // Using prepared statements to prevent SQL injection:
    // 1. Query template with placeholders (?)
    // 2. Parameters bound separately
    // 3. Safe execution guaranteed!
    
    // SECURITY BEST PRACTICES:
    // 1. Using prepared statements prevents SQL injection by separating SQL logic from data
    // 2. The '?' placeholders ensure parameters are properly escaped
    // 3. bind_param() handles proper escaping and type safety
    // 4. Password should be hashed before comparison (TODO: implement password hashing)
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
