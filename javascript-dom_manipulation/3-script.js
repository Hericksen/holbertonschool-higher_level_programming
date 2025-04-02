document.addEventListener("DOMContentLoaded", function () {
  const header = document.querySelector("header");
  const toggleButton = document.getElementById("toggle_header");

  if (header) {
      // Ensure the header starts with one of the classes
      if (!header.classList.contains("red") && !header.classList.contains("green")) {
          header.classList.add("red");
      }
  }

  toggleButton.addEventListener("click", function () {
      if (header.classList.contains("red")) {
          header.classList.replace("red", "green");
      } else {
          header.classList.replace("green", "red");
      }
  });
});
