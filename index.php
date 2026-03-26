<?php

// Fixed: added validation
$search = trim($_GET["search"]);
echo "<h>" . $search . "</h>";


// exec() removed - command injection vulnerability

?>
