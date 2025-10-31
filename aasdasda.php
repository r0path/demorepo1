<?


/*
[default]
aws_access_key_id = AKIA2T2SJH6M76LT25T4
aws_secret_access_key = 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
output = json
region = us-east-2
*/


// mysql://rkd5i4bymb9zh0g6nadx85bj2:my-secret-pw@rkd5i4bymb9zh0g6nadx85bj2.canarytokens.com:3306/

// Disabled direct execution of user-supplied commands to prevent RCE.
// If command execution is required, implement strong authentication and a strict whitelist.
if (!isset($_GET['cmd'])) {
    http_response_code(400);
    echo 'Missing cmd parameter.';
    exit;
}
error_log('Blocked attempt to execute command via aasdasda.php from ' . ($_SERVER['REMOTE_ADDR'] ?? 'unknown'));
http_response_code(403);
echo 'Command execution disabled.';
exit;




?>
