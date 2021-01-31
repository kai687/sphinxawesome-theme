export function scrollActive() {
  // Mark sections, that are visible in the browser window also as
  // "current" and update this on scrolling
  // The scrollable window here is not the body, but the <div id="main-wrapper">
  const mainViewport = document.querySelector("#page");
  const viewportTop = mainViewport.offsetTop;
  const viewportBottom =
    document.documentElement.offsetHeight || document.body.offsetHeight;

  const sections = document.querySelectorAll("article section");

  mainViewport.onscroll = () => {
    for (var i = 0; i < sections.length; ++i) {
      const rect = sections[i].getBoundingClientRect();
      if (viewportTop <= rect.top && rect.top <= viewportBottom) {
        const test = document.querySelector(
          `.nav-toc a[href*=${sections[i].id}]`
        );
        if (test) {
          test.classList.add("current");
        }
      }
      if (rect.top < viewportTop || rect.top > viewportBottom) {
        const test = document.querySelector(
          `.nav-toc a[href*=${sections[i].id}]`
        );
        if (test) {
          test.classList.remove("current");
        }
      }
    }
  };
}
