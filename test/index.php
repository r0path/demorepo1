<?php

$search = isset($_GET["searc"]) ? $_GET["searc"] : '';
echo htmlspecialchars($search, ENT_QUOTES, 'UTF-8');

?>
