<?php
function calculate($a, $b, $operation) {
    switch ($operation) {
        case 'add':
            return $a + $b;
        case 'subtract':
            return $a - $b;
        case 'multiply':
            return $a * $b;
        case 'divide':
            if ($b == 0) {
                throw new Exception("Division by zero");
            }
            return $a / $b;
        default:
            throw new Exception("Invalid operation");
    }
}
echo calculate(10, 5, 'add'); // Output: 15