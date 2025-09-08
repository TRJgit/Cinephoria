document.addEventListener("DOMContentLoaded", function() {
    const arrows = document.querySelectorAll(".arrow");
    const movieLists = document.querySelectorAll(".movie-list");

    arrows.forEach((arrow, i) => {
        const movieListItem = movieLists[i].querySelector(".movie-list-item");
        if (!movieListItem) return; // Skip if the list is empty

        const itemStyle = window.getComputedStyle(movieListItem);
        const itemWidth = movieListItem.offsetWidth + parseInt(itemStyle.marginRight);
        let scrollPosition = 0;

        arrow.addEventListener("click", () => {
            const listWidth = movieLists[i].scrollWidth; // Total width of all items
            const wrapperWidth = movieLists[i].parentElement.offsetWidth; // Visible width of the container
            const maxScroll = listWidth - wrapperWidth; // Maximum scrollable distance

            // Move the list to the left
            scrollPosition -= itemWidth * 3; // Scroll by 3 items at a time for a nice effect

            // If we've scrolled past the end, reset to the beginning
            if (Math.abs(scrollPosition) > maxScroll) {
                scrollPosition = 0;
            }

            movieLists[i].style.transform = `translateX(${scrollPosition}px)`;
        });
    });
});