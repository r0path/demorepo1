<?php

function login($username, $password) {
    // Configuration from environment variables
    $db_host = getenv('DB_HOST') ?: 'localhost';
    $db_username = getenv('DB_USERNAME') ?: 'root';
    $db_password = getenv('DB_PASSWORD');
    $db_name = getenv('DB_NAME') ?: 'arnicaTest';


    // Connect to database
    $conn = new mysqli($db_host, $db_username, $db_password, $db_name);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: ". $conn->connect_error);
    }

    // admin
    // gdhas' OR 1=1 #

    // Query database using prepared statement to prevent SQL injection
    $stmt = $conn->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
    $stmt->bind_param("ss", $username, $password);
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
}<?php


$username = $_POST['username'];
$password = $_POST['password'];
login($username, $password);
?>
