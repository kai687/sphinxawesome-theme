// Functionality for opening and closing the navigation menu

function navFunctions() {
  const nav = document.querySelector("nav");
  const closeNavBtn = document.querySelector("#closeNavBtn");
  const openNavBtn = document.querySelector("#openNavBtn");

  if (openNavBtn) {
    openNavBtn.onclick = () => {
      nav.setAttribute("data-menu", "open");
    };
  }
  if (closeNavBtn) {
    closeNavBtn.onclick = () => {
      nav.setAttribute("data-menu", "closed");
    };
  }
  // We want to close the nav menu also, when clicking on a link in the nav menu on the
  // current page (but only on small screens (i.e., where the close button is visible))
  document.querySelectorAll("nav li.current a").forEach((link) => {
    if (closeNavBtn.offsetWidth > 0 && closeNavBtn.offsetHeight > 0) {
      link.onclick = () => {
        nav.setAttribute("data-menu", "closed");
      };
    }
  });
}

function collapsibleNav() {
  document.querySelectorAll(".expand").forEach((span) => {
    span.onclick = () => {
      span.parentElement.parentElement.classList.toggle("expanded");
    };
  });

  // expand NAV when tab focus is received on link
  const navLinks = document.querySelectorAll("#nav-toc a");
  navLinks.forEach((navLink) => {
    navLink.onfocus = (e) => {
      document.querySelectorAll(".expand").forEach((span) => {
        const li = span.parentElement.parentElement;
        if (li.contains(e.target)) {
          li.classList.add("expanded");
        } else {
          if (!li.classList.contains("current")) {
            li.classList.remove("expanded");
          }
        }
      });
    };
  });
}

export { navFunctions, collapsibleNav };
