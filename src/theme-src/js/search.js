import { hideSnackbar } from "./snackbar";

// Some enhancements for the search experience
export function searchPane() {
  const searchPane = document.querySelector("#search-pane");
  const openSearchBtn = document.querySelector("#openSearchBtn");
  const closeSearchBtn = document.querySelector("#closeSearchBtn");
  const searchPaneShownClass = "searchPaneIsShown";

  if (openSearchBtn) {
    openSearchBtn.onclick = () => {
      searchPane.classList.add(searchPaneShownClass);
    };
  }
  if (closeSearchBtn) {
    closeSearchBtn.onclick = () => {
      searchPane.classList.remove(searchPaneShownClass);
    };
  }
}

export function clearSearchHighlights() {
  setTimeout(() => {
    const snackbar = document.querySelector("#snackbar");
    const highlights = document.querySelectorAll(".highlighted");
    const searchInput = document.querySelector("#search-input");

    if (highlights.length) {
      snackbar.innerHTML =
        '<a class="tracking-wide" href="javascript:Documentation.hideSearchWords()">' +
        _("Clear highlighted search results") +
        "</a>";
      snackbar.style.opacity = 1;
      snackbar.style.transform = "translate(0,0)";

      document.querySelector("#snackbar > a").onclick = () => {
        hideSnackbar();
        searchInput.value = "";
      };

      // Add the currently searched for term in the input
      searchInput.value = highlights[0].textContent;
      searchInput.onsearch = () => {
        Documentation.hideSearchWords();
        hideSnackbar();
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
