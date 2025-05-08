<?php
$name=$_GET['name'];
echo "welcome $name";
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Handling</title>
</head>
<body>
    <form action="3.php" method="GET">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>