<?php
session_start();
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "users_data";

$conn = new mysqli($servername, $username, $password, $dbname);


if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $email = $_POST['email'];
    $password = $_POST['password'];


    $stmt = $conn->prepare("SELECT password FROM users WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows > 0) {
        $stmt->bind_result($hashed_password);
        $stmt->fetch();

        // Verify password
        if (password_verify($password, $hashed_password)) {
            $_SESSION['email'] = $email; 
            echo "Login successful! Redirecting...";
            header("refresh:2;url=index.html");
        } else {
            echo "Invalid password!";
        }
    } else {
        echo "No account found with that email!";
    }

    $stmt->close();
}

$conn->close();
?>
