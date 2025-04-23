<?php
// Develop a PHP script that validates the entered login credentials (username and password) against the database records. If valid, allow the user to log in
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "data";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $inputUsername = $_POST['username'] ?? '';
    $inputPassword = $_POST['password'] ?? '';

    if ($inputUsername && $inputPassword) {
        $stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
        if ($stmt) {
            $stmt->bind_param("s", $inputUsername);
            $stmt->execute();
            $result = $stmt->get_result();
            $user = $result->fetch_assoc();

            if ($user && $inputPassword == $user['password']) {
            echo "Login successful! Welcome, " . htmlspecialchars($user['username']) . ".";
            } else {
            echo "<p style='color: red;'>Invalid username or password.</p>";
            }
            $stmt->close();
        } else {
            echo "<p style='color: red;'>Query preparation failed.</p>";
        }
    } else {
        echo "<p style='color: red;'>Both fields are required.</p>";
    }
}

$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <form method="post">
        <label>Username:</label>
        <input type="text" name="username">
        <br><br>
        <label>Password:</label>
        <input type="password" name="password">
        <br><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
