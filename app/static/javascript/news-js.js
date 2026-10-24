const newsTemplate = document.querySelector("#news-template");

function createNewsCard(article) {
    const newCard = newsTemplate.content.cloneNode(true);
}


function setupCarouselTrack() {
    const carouselContainers = document.querySelectorAll(".carousel-container");

    carouselContainers.forEach(carouselContainer => {
        
        const prevBtn = carouselContainer.parentElement.querySelector(
            ":scope > .prev-btn"
        );

        const nextBtn = carouselContainer.parentElement.querySelector(
            ":scope > .next-btn"
        );

        const scrollDistance = carouselContainer.clientWidth;

        nextBtn.addEventListener("click", () => {
            carouselContainer.scrollBy({
                left: scrollDistance,
                behavior: "smooth"
            });
        });

        prevBtn.addEventListener("click", () => {
            carouselContainer.scrollBy({
                left: -scrollDistance,
                behavior: "smooth"
            });
        });
    });
}

setupCarouselTrack();
