document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("update_header").addEventListener("click", function () {
      const header = document.querySelector("header");
      if (header) {
          header.textContent = "New Header!!!";
      }
  });
});
