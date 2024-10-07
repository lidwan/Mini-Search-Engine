const btn = document.querySelector(".search-btn");

btn.addEventListener("click", Search);


function Search() {
    const div = document.querySelector(".test");
    div.textContent = "THIS IS WORKING!!";
}