<?php
require 'config.php';

$data = json_decode(file_get_contents("php://input"), true);

if (isset($data['voltage']) && isset($data['current'])) {
    $voltage = floatval($data['voltage']);
    $current = floatval($data['current']);

    $stmt = $conn->prepare("INSERT INTO predictions (voltage, current) VALUES (?, ?)");
    $stmt->bind_param("dd", $voltage, $current);

    if ($stmt->execute()) {
        echo json_encode(["status" => "success", "message" => "Predictions stored successfully"]);
    } else {
        echo json_encode(["status" => "error", "message" => "Failed to store predictions"]);
    }

    $stmt->close();
} else {
    echo json_encode(["status" => "error", "message" => "Invalid input data"]);
}

$conn->close();
?>
