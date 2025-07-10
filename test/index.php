<?php

require_once __DIR__ . '/sanitize.php';

$search = isset($_GET['searc']) ? sanitize($_GET['searc']) : '';
echo $search;

?>
