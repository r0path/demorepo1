<?php

echo htmlspecialchars(isset($_GET["searc"]) ? $_GET["searc"] : '', ENT_QUOTES, 'UTF-8');

?>
