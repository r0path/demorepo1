<?php

$search = isset($_GET["searc"]) ? htmlspecialchars($_GET["searc"], ENT_QUOTES, 'UTF-8') : '';
echo $search;

?>
