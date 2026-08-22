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


