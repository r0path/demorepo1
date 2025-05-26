<?php

// Fix XSS vulnerability by:
// 1. Adding isset() check to prevent undefined index errors
// 2. Using htmlspecialchars() to escape special characters
$search = isset($_GET["searc"]) ? $_GET["searc"] : '';
echo htmlspecialchars($search, ENT_QUOTES, 'UTF-8');

?>
