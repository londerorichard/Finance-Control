function hideSearchBar() {
    const searchBar = document.querySelector(".search-input");
    const searchBtn = document.querySelector(".search-btn");

    searchBtn.addEventListener("click", () => {
        searchBar.classList.toggle("hidden");
    });
}

hideSearchBar();