function hideSearchBar() {
    const searchBar = document.querySelector(".search-input");
    const searchBtn = document.querySelector(".search-btn");

    searchBtn.addEventListener("click", () => {
        searchBar.classList.toggle("hidden");
    });
}
hideSearchBar();


function hideNotifications() {
    const notifPanel = document.querySelector(".notification-panel");
    const profilePanel = document.querySelector(".profile-panel");
    const notifBtn = document.querySelector(".notification-btn");

    notifBtn.addEventListener("click", () => {
        profilePanel.classList.add("hidden");
        notifPanel.classList.toggle("hidden");
    });
}

hideNotifications();

function hideSettings() {
    const notifPanel = document.querySelector(".notification-panel");
    const profilePanel = document.querySelector(".profile-panel");
    const profileBtn = document.querySelector(".profile-btn");

    profileBtn.addEventListener("click", () => {
        notifPanel.classList.add("hidden");
        profilePanel.classList.toggle("hidden");
    });
}

hideSettings();