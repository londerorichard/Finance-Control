const newsTemplate = document.querySelector("#news-template");

function createNewsCard(article) {
    const newCard = newsTemplate.content.cloneNode(true);

    const title = newCard.querySelector(".title");
    const description = newCard.querySelector(".description");
    const date = newCard.querySelector(".date");
    const source = newCard.querySelector(".source span");
    const articleUrl = newCard.querySelector(".article-url");
    const image = newCard.querySelector(".image");

    // Article title and description
    title.textContent = article.title || "Untitled article";
    description.textContent =
        article.description || "No description available.";

    // Format publication date
    if (article.published_at) {
        const publishedDate = new Date(article.published_at);

        date.textContent = Number.isNaN(publishedDate.getTime())
            ? "Date unavailable"
            : new Intl.DateTimeFormat("en", {
                  year: "numeric",
                  month: "short",
                  day: "numeric",
              }).format(publishedDate);
    } else {
        date.textContent = "Date unavailable";
    }

    // News source
    source.textContent = article.source || "Unknown source";

    // Article URL
    try {
        const url = new URL(article.url);

        if (["https:", "http:"].includes(url.protocol)) {
            articleUrl.href = url.href;
        } else {
            articleUrl.removeAttribute("href");
        }
    } catch {
        articleUrl.removeAttribute("href");
    }

    // Article image
    image.alt = article.title
        ? `Image for ${article.title}`
        : "News article image";

    if (article.image_url) {
        image.src = article.image_url;

        image.addEventListener(
            "error",
            () => {
                image.hidden = true;
            },
            { once: true }
        );
    } else {
        image.hidden = true;
    }

    return newCard;
}


function renderNews(articles) {
    const newsList = document.querySelector(".news-list");

    if (!newsList) {
        console.error("News list element was not found.");
        return;
    }

    newsList.replaceChildren();

    if (!articles || articles.length === 0) {
        const message = document.createElement("li");
        message.classList.add("news-message");
        message.textContent = "No news articles available.";

        newsList.appendChild(message);

        newsList.dispatchEvent(
            new Event("newsrendered", { bubbles: true })
        );

        return;
    }

    articles.forEach((article) => {
        const newsCard = createNewsCard(article);
        newsList.appendChild(newsCard);
    });

    newsList.dispatchEvent(
        new Event("newsrendered", { bubbles: true })
    );
}


async function loadNews() {
    const token = localStorage.getItem("access_token");

    if (!token) {
        console.error("Authentication token was not found.");
        return;
    }

    const newsList = document.querySelector(".news-list");

    try {
        if (newsList) {
            newsList.replaceChildren();

            const loadingMessage = document.createElement("li");
            loadingMessage.classList.add("news-message");
            loadingMessage.textContent = "Loading financial news...";

            newsList.appendChild(loadingMessage);
        }

        const data = await getFinancialNews(token);

        renderNews(data.articles);
    } catch (error) {
        console.error("Failed to load financial news:", error);

        if (newsList) {
            newsList.replaceChildren();

            const errorMessage = document.createElement("li");
            errorMessage.classList.add("news-message");
            errorMessage.textContent =
                "Unable to load financial news. Please try again later.";

            newsList.appendChild(errorMessage);

            newsList.dispatchEvent(
                new Event("newsrendered", { bubbles: true })
            );
        }
    }
}


function setupCarouselTrack() {
    const carouselContainers = document.querySelectorAll(".carousel-container");

    carouselContainers.forEach((carouselContainer) => {
        const carousel = carouselContainer.parentElement;

        const prevBtn = carousel.querySelector(":scope > .prev-btn");
        const nextBtn = carousel.querySelector(":scope > .next-btn");

        if (!prevBtn || !nextBtn) {
            console.warn("Carousel navigation buttons were not found.");
            return;
        }

        function updateButtonStates() {
            const maxScrollLeft =
                carouselContainer.scrollWidth - carouselContainer.clientWidth;

            const hasOverflow = maxScrollLeft > 1;

            prevBtn.disabled =
                !hasOverflow || carouselContainer.scrollLeft <= 1;

            nextBtn.disabled =
                !hasOverflow ||
                carouselContainer.scrollLeft >= maxScrollLeft - 1;
        }

        function scrollCarousel(direction) {
            const scrollDistance = carouselContainer.clientWidth;

            carouselContainer.scrollBy({
                left: scrollDistance * direction,
                behavior: "smooth",
            });
        }

        prevBtn.addEventListener("click", () => {
            scrollCarousel(-1);
        });

        nextBtn.addEventListener("click", () => {
            scrollCarousel(1);
        });

        carouselContainer.addEventListener("scroll", updateButtonStates);

        window.addEventListener("resize", updateButtonStates);

        updateButtonStates();

        carouselContainer.addEventListener(
            "newsrendered",
            updateButtonStates
        );
    });
}


setupCarouselTrack();
loadNews();