<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "data";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT  name,email FROM data";
$result = $conn->query($sql);
if($result->num_rows > 0) {
while($row = $result->fetch_assoc()) {
    echo "Name: " . $row["name"]. " - Email: " . $row["email"]. "<br>";
}
} else {
    echo "0 results";
}
$conn->close();
?>

