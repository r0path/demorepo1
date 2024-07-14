<?php

<?php

// Include utility functions
include 'utils.php';

/**
 * Sanitize the user input from the GET request
 * This helps prevent XSS attacks by converting special characters to HTML entities.
 */
echo sanitize_input($_GET["search"]);

?>

?>
