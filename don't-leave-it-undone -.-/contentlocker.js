document.addEventListener("DOMContentLoaded", function() {
    const steps = document.querySelectorAll('.step');
    const buttons = document.querySelectorAll('.next-btn');

    buttons.forEach((button, index) => {
        button.addEventListener('click', function() {
            steps[index].style.display = 'none'; // Hide current step
            steps[index + 1].style.display = 'block'; // Show next step
        });
    });
});
