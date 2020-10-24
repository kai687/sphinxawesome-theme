// Functionality for opening and closing the navigation menu

function navFunctions() {
  const nav = document.querySelector('nav[role="navigation"]');
  const body = document.querySelector("body");
  const screen = document.querySelector("#screen");
  const closeNavBtn = document.querySelector("#closeNavBtn");
  const openNavBtn = document.querySelector("#openNavBtn");

  if (openNavBtn) {
    openNavBtn.onclick = () => {
      nav.setAttribute("data-menu", "open");
      body.style.overflow = "hidden";
      screen.style.display = "initial";
    };
  }
  if (closeNavBtn) {
    closeNavBtn.onclick = () => {
      nav.setAttribute("data-menu", "closed");
      body.style.removeProperty("overflow");
      screen.style.display = "none";
    };
  }

  screen.onclick = () => {
    nav.setAttribute("data-menu", "closed");
    body.style.removeProperty("overflow");
    screen.style.display = "none";
  };

  // close the nav menu when clicking on a nav link on the current page
  document.querySelectorAll(".nav-toc li.current a").forEach((link) => {
    if (nav.getAttribute("data-menu") === "open") {
      link.onclick = () => {
        nav.setAttribute("data-menu", "closed");
        body.style.removeProperty("overflow");
        screen.style.display = "none";
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
  const navLinks = document.querySelectorAll(".nav-toc a");
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
