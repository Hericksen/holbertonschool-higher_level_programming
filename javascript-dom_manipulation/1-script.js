document.addEventListener("DOMContentLoaded", function () {
  // Select the element with id "red_header"
  let redHeader = document.getElementById("red_header");

  // Select the <header> element
  let header = document.querySelector("header");

  // Add a click event listener
  redHeader.addEventListener("click", function () {
      // Change the text color of the header to red
      header.style.color = "#FF0000";
  });
});
