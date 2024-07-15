<?php
require_once 'utils.php';

// Start output buffering
ob_start();

// Reflect all GET parameters
foreach ($_GET as $key => $value) {
    echo "<p><strong>" . sanitize_input($key) . ":</strong> " . sanitize_input($value) . "</p>";
}

// Get the content
$content = ob_get_clean();

// Output the HTML
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GET Parameters Reflection</title>
</head>
<body>
    <h1>GET Parameters Reflection</h1>
    <?php
    if (empty($content)) {
        echo "<p>No GET parameters were provided.</p>";
    } else {
        echo $content;
    }
    ?>
</body>
</html>
