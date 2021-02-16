export function scrollActive() {
  // Mark the currently visible section as active in the sidebar
  // Use the `IntersectionObserver` API
  const sections = document.querySelectorAll("article section");
  const options = {
    rootMargin: "-45% 0px -45% 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    const section = entries[0].target;
    // find the link in the sidebar that matches the section ID
    const matchingNavLink = document.querySelector(
      `.nav-toc a[href*=${section.id}]`
    );
    if (matchingNavLink) {
      matchingNavLink.classList.toggle("current");
    }
  }, options);

  sections.forEach((section) => {
    observer.observe(section);
  });
}

export function scrollToTop() {
  const scrollTop = document.querySelector("#scrolltop");

  if (!scrollTop) {
    return;
  }

  const main = document.querySelector("main");

  main.onscroll = () => {
    if (main.scrollTop > 100) {
      scrollTop.classList.add("isShown");
    } else {
        scrollTop.classList.remove("isShown");
    }
  };

  scrollTop.onclick = () => {
    main.scrollTop = 0;
  };
}
