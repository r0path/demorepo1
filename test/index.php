<?php

// Sanitize the search parameter to prevent XSS attacks
// Using htmlspecialchars with ENT_QUOTES to encode both single and double quotes
// UTF-8 encoding ensures proper handling of special characters
echo htmlspecialchars($_GET["search"], ENT_QUOTES, 'UTF-8');

?>
