<?php
$servername = "localhost";
$db_username = "root"; 
$db_password = "Poornima16@23";
$dbname = "student";

$conn = new mysqli($servername, $db_username, $db_password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$name = $_POST['name'];
$user_input_username = $_POST['uname']; 
$password = $_POST['pword'];
$age = $_POST['age'];
$hobbies = $_POST['hobbies'];

$hashed_password = password_hash($password, PASSWORD_DEFAULT);

$stmt = $conn->prepare("INSERT INTO users 
(name, username, password, age, hobbies) VALUES (?, ?, ?, ?, ?)");
$stmt->bind_param("sssss",
 $name, $user_input_username, $hashed_password, $age, $hobbies); 

if ($stmt->execute()) {
    echo "Registration successful!";
} else {
    echo "Error: " . $stmt->error;
}

$stmt->close();
$conn->close();
?>
