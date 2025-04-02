document.getElementById("add_item").addEventListener("click", function() {
  // Create a new <li> element
  let newItem = document.createElement("li");
  newItem.textContent = "Item";

  // Append the new item to the <ul> with class "my_list"
  document.querySelector(".my_list").appendChild(newItem);
});
