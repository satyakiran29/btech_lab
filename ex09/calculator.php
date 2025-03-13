<?php
function calculator($num1, $num2, $op) {
switch ($op) {
    case "add":
        return $num1 + $num2;
        break;  
    case "sub":    
        return $num1 - $num2;
        break;
    case "mul":
        return $num1 * $num2;
        break;
    case "div":
        return $num1!=$num2 ? $num1 / $num2 : "Division by zero is not possible";
        break;
   default:
        return "Invalid operator";
        break;    
}
echo calculator(5, 10, "div");