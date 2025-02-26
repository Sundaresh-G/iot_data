<?php
require 'config.php';

$sql = "SELECT voltage, current, created_at FROM predictions ORDER BY id DESC LIMIT 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo json_encode($result->fetch_assoc());
} else {
    echo json_encode(["status" => "error", "message" => "No predictions found"]);
}

$conn->close();
?>
