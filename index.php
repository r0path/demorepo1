<?php

// Include utility functions
include 'utils.php';

// Sanitize the user input from the GET request
echo sanitize_input($_GET["search"]);

?>
