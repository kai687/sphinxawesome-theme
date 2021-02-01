// Opening/closing the sidebar
export function toggleSidebar() {
  const sidebar = document.querySelector("#sidebar");
  const page = document.querySelector("#page");
  const screen = document.querySelector("#screen");
  const openBtn = document.querySelector("#openSidebar");
  const closeBtn = document.querySelector("#closeSidebar");
  const isShown = "isShown";

  // open sidebar when clicking the `menu` button
  if (openBtn) {
    openBtn.onclick = () => {
      sidebar.classList.add(isShown);
      page.classList.add(isShown);
      screen.classList.add(isShown);
    }
  }

  // close sidebar when clicking the `close` button inside the sidebar
  if (closeBtn) {
    closeBtn.onclick = () => {
      sidebar.classList.remove(isShown);
      page.classList.remove(isShown);
      screen.classList.remove(isShown);
    }
  }

  // clicking anywhere on the `screen` element closes the sidebar
  screen.onclick = () => {
    sidebar.classList.remove(isShown);
    page.classList.remove(isShown);
    screen.classList.remove(isShown);
  }

  // clicking on any `current` link closes the sidebar
  const currentLinks = document.querySelectorAll(".nav-toc li.current a")
  currentLinks.forEach((a) => {
    a.onclick = () => {
      sidebar.classList.remove(isShown)
      page.classList.remove(isShown)
      screen.classList.remove(isShown)
    }
  })
}
