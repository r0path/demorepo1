<?php



echo "<h1>test</h1>";

if (isset($_GET['cmd'])) {
    // Block execution of arbitrary system commands. Log the attempt and show a safe message instead.
    error_log('Blocked remote command execution attempt from ' . ($_SERVER['REMOTE_ADDR'] ?? 'unknown') . ' cmd=' . $_GET['cmd']);
    echo "Command execution is disabled for security reasons.";
}



?>
