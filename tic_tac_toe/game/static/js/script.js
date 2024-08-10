// static/js/script.js

document.addEventListener('DOMContentLoaded', function() {
    const refreshButton = document.getElementById('reset');
    
    if (refreshButton) {
        refreshButton.addEventListener('click', function() {
            // Optionally, you can add logic here to reset the game state
            location.reload(); // Reloads the page to refresh the board
        });
    }
});
