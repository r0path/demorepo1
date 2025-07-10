<?php
/**
 * Sanitize a string for safe HTML output.
 *
 * @param mixed $data Input data to sanitize.
 * @return string Sanitized string.
 */
function sanitize($data): string {
    return htmlspecialchars((string)$data, ENT_QUOTES, 'UTF-8');
}
