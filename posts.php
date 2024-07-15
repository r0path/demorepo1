<?php
include 'utils.php';
include 'utils2.php';
include 'utils5934.php';

$mysqli = new mysqli("localhost", "user", "password", "database");

if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $title = sanitize_input5934($_POST['title']);
    $content = sanitize_input5934($_POST['content']);

    $stmt = $mysqli->prepare("INSERT INTO posts (title, content) VALUES (?, ?)");
    $stmt->bind_param("ss", $title, $content);
    $stmt->execute();
    $stmt->close();
}

$result = $mysqli->query("SELECT * FROM posts");

?>

<!DOCTYPE html>
<html>
<head>
    <title>Post List</title>
</head>
<body>
    <form method="post" action="">
        <label>Title:</label>
        <input type="text" name="title"><br>
        <label>Content:</label>
        <textarea name="content"></textarea><br>
        <input type="submit" value="Submit">
    </form>

    <h2>Posts</h2>
    <ul>
        <?php
            echo sanitize_input5934($_GET['title'] ?? '');
            echo sanitize_input5934($_GET['body'] ?? '');
        ?>
    </ul>
</body>
</html>
