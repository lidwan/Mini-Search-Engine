const btn = document.querySelector(".search-btn");

btn.addEventListener("click", search);


async function search() {
    const query = document.querySelector(".search-query").value;
    const response = await fetch('#');
    const results = await response.json();

    const resultsDiv = document.querySelector(".results");
    resultsDiv.innerHTML = '';
    
    results.forEach(article => {
        const articleDiv = document.createElement('div');
        articleDiv.innerHTML = `<h2>${article.title}</h2><p>${article.content}</p><a href="${article.link}" target="_blank">Read more</a>`;
        resultsDiv.appendChild(articleDiv);
    });
}
