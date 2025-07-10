<?php
/**
 * Sanitize input to prevent XSS.
 *
 * @param string $input
 * @return string
 */
function sanitize(string $input): string {
    return htmlspecialchars($input, ENT_QUOTES, 'UTF-8');
}
