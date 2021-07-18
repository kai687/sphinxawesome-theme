export function scrollActive() {
  // Mark the currently visible section as active in the sidebar
  // Use the `IntersectionObserver` API
  const sections = document.querySelectorAll("article section");
  const options = {
    root: document.querySelector("main"),
    rootMargin: "0px 0px -95% 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const matchingLink = document.querySelector(
          `.nav-toc a[href*=${entry.target.id}]`
        );
        matchingLink.classList.add("current");
      } else {
        const matchingLink = document.querySelector(
          `.nav-toc a[href*=${entry.target.id}]`
        );
        matchingLink.classList.remove("current");
      }
    });
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
    scrollTop.blur();
  };
}
