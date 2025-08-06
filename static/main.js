// Navigation function
function navigateToTool(toolName) {
    window.location.href = `${toolName}.html`;
}

// Back to home function
function goBack() {
    window.location.href = 'index.html';
}

// Common utility functions
function showResult(elementId, message) {
    const resultDiv = document.getElementById(elementId);
    if (resultDiv) {
        resultDiv.textContent = message;
        resultDiv.style.display = 'block';
    }
}

function clearResult(elementId) {
    const resultDiv = document.getElementById(elementId);
    if (resultDiv) {
        resultDiv.style.display = 'none';
    }
}

// Add smooth scrolling for better UX
document.addEventListener('DOMContentLoaded', function() {
    // Add loading animation
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 100);
});