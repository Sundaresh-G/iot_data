async function fetchPredictions() {
    const response = await fetch('/php/get_predictions.php');
    const data = await response.json();

    if (data.voltage && data.current) {
        document.getElementById('voltage').textContent = data.voltage.toFixed(2);
        document.getElementById('current').textContent = data.current.toFixed(2);
    } else {
        console.error("Failed to load predictions");
    }
}

setInterval(fetchPredictions, 5000);
