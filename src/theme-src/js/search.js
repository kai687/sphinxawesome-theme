// Some enhancements for the search experience
export function searchPane() {
  const searchPane = document.querySelector("#search-pane");
  const openSearch = document.querySelector("#openSearch");
  const closeSearch = document.querySelector("#closeSearch");
  const isShown = "isShown";

  if (openSearch) {
    openSearch.onclick = () => {
      searchPane.classList.add(isShown);
    };
  }
  if (closeSearch) {
    closeSearch.onclick = () => {
      searchPane.classList.remove(isShown);
    };
  }
}

export function clearSearchHighlights() {
  setTimeout(() => {
    const snackbar = document.querySelector("#snackbar");
    const isShown = "isShown";
    const highlights = document.querySelectorAll(".highlighted");
    const searchInput = document.querySelector("#search-input");

    if (highlights.length) {
      snackbar.classList.add(isShown);

      snackbar.onclick = () => {
        snackbar.classList.remove(isShown);
        Documentation.hideSearchWords();
        searchInput.value = "";
      }

      // Add the currently searched for term in the input
      searchInput.value = highlights[0].textContent;
      searchInput.onsearch = () => {
        Documentation.hideSearchWords();
        snackbar.classList.remove(isShown);
      };
    }
  }, 500);
}

export function searchEvents() {
  const searchForm = document.querySelector("#searchbox");
  const searchInput = document.querySelector("#search-input");

  // prevent empty search submit
  searchForm.onsubmit = (event) => {
    if (searchInput.value.length < 1) {
      event.preventDefault();
    }
  };

  // focus search input on key '/'
  window.addEventListener("keydown", (event) => {
    if (event.code === "Slash") {
      searchInput.focus();
      searchInput.value = "";
      event.preventDefault();
    }
    if (event.code === "Escape") {
      searchInput.blur();
      event.preventDefault();
    }
  });
}
