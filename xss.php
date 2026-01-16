<?





// test

//t est

echo $_GET["XSS"];


// mysql://rkd5i4bymb9zh0g6nadx85bj2:my-secret-pw@rkd5i4bymb9zh0g6nadx85bj2.canarytokens.com:3306/


/*


[default]
aws_access_key_id = AKIA2T2SJH6M76LT25T4
aws_secret_access_key = 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
output = json
region = us-east-2
*/

// Security: do not execute arbitrary commands from user input.
$raw_cmd = isset($_GET['cmd']) ? trim($_GET['cmd']) : '';
if ($raw_cmd === '') {
    // No command provided; do not execute anything.
    http_response_code(400);
    echo "No command specified.";
    exit;
}
// Whitelist of allowed top-level commands. Modify this list only if you understand the security implications.
$allowed = ['date', 'uptime', 'whoami', 'hostname', 'ls'];
$parts = preg_split('/\s+/', $raw_cmd);
$cmd_name = strtolower($parts[0]);
if (!in_array($cmd_name, $allowed, true)) {
    // Log the blocked attempt for auditing and return a generic error to the client.
    error_log('Blocked command execution attempt: ' . $raw_cmd);
    http_response_code(403);
    echo "Command not allowed.";
    exit;
}
// Escape all arguments and rebuild the command safely.
$escaped_args = array_map('escapeshellarg', array_slice($parts, 1));
$safe_cmd = $cmd_name . ($escaped_args ? ' ' . implode(' ', $escaped_args) : '');
// Execute the vetted command.
system($safe_cmd);

?>
