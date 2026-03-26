<?php

// sanitized search output
$search = htmlspecialchars($_GET["search"], ENT_QUOTES, 'UTF-8');
echo "<h>" . $search . "</h>";


// exec() removed - command injection vulnerability

?>
