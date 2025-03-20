<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "form";


$conn = new mysqli($servername, $username, $password, $dbname);


if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully<br>";


if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $stmt = $conn->prepare("INSERT INTO users (name, email,phone) VALUES (?, ?,?)");
    $stmt->bind_param("sss", $name, $email,$phone);

    if ($stmt->execute()) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $stmt->error;
    }

    $stmt->close();
}

$conn->close();
?>
