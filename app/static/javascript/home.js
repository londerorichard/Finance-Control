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
    const notifBtn = document.querySelector(".notification-btn");

    notifBtn.addEventListener("click", () => {
        notifPanel.classList.toggle("hidden")
    });
}
hideNotifications();


function hideSettings() {
    const profilePanel = document.querySelector(".profile-panel");
    const profilefBtn = document.querySelector(".profile-btn");

    profilefBtn.addEventListener("click", () => {
        profilePanel.classList.toggle("hidden")
    });
}
hideSettings();