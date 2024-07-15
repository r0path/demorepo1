<?php

function sanitize_input($input) {
    return htmlspecialchars($input ?? '', ENT_QUOTES, 'UTF-8');
}
