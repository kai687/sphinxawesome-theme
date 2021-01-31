// Opening/closing the sidebar
export function toggleSidebar() {
  const sidebar = document.querySelector("#sidebar");
  const page = document.querySelector("#page");
  const screen = document.querySelector("#screen");
  const openNavBtn = document.querySelector("#openNavBtn");
  const closeNavBtn = document.querySelector("#closeNavBtn");
  const navShownClass = "sidebarIsShown"

  // open sidebar when clicking the `menu` button
  if (openNavBtn) {
    openNavBtn.onclick = () => {
      sidebar.classList.add(navShownClass);
      page.classList.add(navShownClass);
      screen.classList.add(navShownClass);
    }
  }

  // close sidebar when clicking the `close` button inside the sidebar
  if (closeNavBtn) {
    closeNavBtn.onclick = () => {
      sidebar.classList.remove(navShownClass);
      page.classList.remove(navShownClass);
      screen.classList.remove(navShownClass);
    }
  }

  // clicking anywhere on the `screen` element closes the sidebar
  screen.onclick = () => {
    sidebar.classList.remove(navShownClass);
    page.classList.remove(navShownClass);
    screen.classList.remove(navShownClass);
  }

  // clicking on any `current` link closes the sidebar
  const currentLinks = document.querySelectorAll(".nav-toc li.current a")
  currentLinks.forEach((a) => {
    a.onclick = () => {
      sidebar.classList.remove(navShownClass)
      page.classList.remove(navShownClass)
      screen.classList.remove(navShownClass)
    }
  })
}
