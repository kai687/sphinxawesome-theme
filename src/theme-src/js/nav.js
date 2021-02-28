// collapse / expand the navigation sections inside the sidebar

export function collapsibleNav() {
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
