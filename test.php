<?php

function login($username, $password) {
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

    // admin
    // gdhas' OR 1=1 #

    // Prepare and bind parameters to prevent SQL injection
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
}

$username = $_POST['username'];
$password = $_POST['password'];
login($username, $password);
?>
