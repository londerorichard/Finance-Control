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


function carousel() {

    const track = document.querySelector(".carousel-track");

    const nextButton = document.querySelector(".next-btn");
    const prevButton = document.querySelector(".prev-btn");

    const cards = document.querySelectorAll(".news-card");

    if (cards.length === 0) return;

    let currentIndex = 0;

    const cardWidth = cards[0].offsetWidth;
    const gap = parseInt(getComputedStyle(track).gap);

    const moveAmount = cardWidth + gap;
    const maxIndex = cards.length - 3;

    function updateCarousel() {
        track.style.transform =
            `translateX(-${currentIndex * moveAmount}px)`;
    }

    nextButton.addEventListener("click", () => {

        if(currentIndex >= maxIndex){
            currentIndex = 0;
        } else {
            currentIndex++;
        }

        updateCarousel();

    });

    prevButton.addEventListener("click", () => {

        if(currentIndex <= 0){
            currentIndex = maxIndex;
        } else {
            currentIndex--;
        }

        updateCarousel();

    });

}

carousel();