<?php
$host = "your_database_host";
$username = "your_db_username";
$password = "your_db_password";
$dbname = "your_database_name";

$conn = new mysqli($host, $username, $password, $dbname);

if ($conn->connect_error) {
    die(json_encode(["status" => "error", "message" => "Database connection failed: " . $conn->connect_error]));
}
?>
