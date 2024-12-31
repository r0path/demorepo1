<?php

echo "<p>" . htmlspecialchars($_GET["search"] ?? '', ENT_QUOTES, 'UTF-8') . "</p>";

?>
