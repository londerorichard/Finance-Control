function hideSearchBar() {
    const searchBar = document.querySelector(".search-input");
    const searchBtn = document.querySelector(".search-btn");
    const notifPanel = document.querySelector(".notification-panel");
    const profilePanel = document.querySelector(".profile-panel");

    searchBtn.addEventListener("click", () => {
        searchBar.classList.toggle("hidden");
        profilePanel.classList.add("hidden");
        notifPanel.classList.add("hidden");
    });
}
hideSearchBar();


function hideNotifications() {
    const notifPanel = document.querySelector(".notification-panel");
    const profilePanel = document.querySelector(".profile-panel");
    const notifBtn = document.querySelector(".notification-btn");
    const searchBar = document.querySelector(".search-input");

    notifBtn.addEventListener("click", () => {
        profilePanel.classList.add("hidden");
        notifPanel.classList.toggle("hidden");
        searchBar.classList.add("hidden");
    });
}

hideNotifications();

function hideSettings() {
    const notifPanel = document.querySelector(".notification-panel");
    const profilePanel = document.querySelector(".profile-panel");
    const profileBtn = document.querySelector(".profile-btn");
    const searchBar = document.querySelector(".search-input");

    profileBtn.addEventListener("click", () => {
        notifPanel.classList.add("hidden");
        profilePanel.classList.toggle("hidden");
        searchBar.classList.add("hidden");
    });
}

hideSettings();

function showSideBar() {
    const button = document.querySelector(".sidebar-window-btn");
    const container = document.querySelector(".main-container");

    button.addEventListener("click", () => {
        container.classList.toggle("collapsed");
    });
}

showSideBar();