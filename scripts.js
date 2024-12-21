document.addEventListener("DOMContentLoaded", function() {
    const goldPriceElement = document.getElementById("gold-price");

    async function fetchGoldPrice() {
        try {
            const response = await fetch('/api/gold-price');
            const data = await response.json();
            if (data.price) {
                goldPriceElement.textContent = `$${data.price.toFixed(2)} (${data.currency})`;
            } else {
                goldPriceElement.textContent = "Error fetching price.";
            }
        } catch (error) {
            console.error("Error fetching gold price:", error);
            goldPriceElement.textContent = "Error fetching price.";
        }
    }

    fetchGoldPrice();
});

