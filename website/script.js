const btn = document.querySelector(".search-btn");

btn.addEventListener("click", search);


async function search() {
    const query = document.querySelector(".search-query").value;

    const div = document.querySelector(".test");
    div.textContent = query;
}