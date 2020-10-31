// action for collapsible definition lists
export function collapsible() {
  // clicking on the <dt> expands the section
  document.querySelectorAll(".accordion").forEach((acc) => {
    acc.onclick = (event) => {
      const target = event.target;
      target.classList.toggle("active");
      const isExpanded = target.getAttribute("aria-expanded") === "true"
      if (isExpanded) {
        target.setAttribute("aria-expanded", "false")
      } else {
        target.setAttribute("aria-expanded", "true")
      }
    };
  });

  // clicking on the `expand-more` button expands the section
  document.querySelectorAll(".accordion .expand-more").forEach((btn) => {
    btn.onclick = (event) => {
      const dt = event.target.parentNode;
      dt.classList.toggle("active");
      const isExpanded = dt.getAttribute("aria-expanded") === "true"
      if (isExpanded) {
        dt.setAttribute("aria-expanded", "false")
      } else {
        dt.setAttribute("aria-expanded", "true")
      }
    };
  });
}
