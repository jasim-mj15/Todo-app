document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".done-btn").forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent full page reload
            let taskItem = this.closest("li"); // Get parent <li>
            taskItem.classList.add("removed"); // Apply fade-out effect
            setTimeout(() => {
                this.parentElement.submit(); // Submit form after animation
            }, 300);
        });
    });
});
