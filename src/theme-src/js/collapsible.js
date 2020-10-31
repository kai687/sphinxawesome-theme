function collapse(element) {
  // "element" should be the <dt> with the icon.
  element.classList.toggle("active");
  const btn = element.querySelector("button.expand-more")
  if (element.classList.contains("active")) {
    btn.setAttribute("aria-expanded", "true");
    btn.setAttribute("aria-label", "Collapse this section");
  } else {
    btn.setAttribute("aria-expanded", "false");
    btn.setAttribute("aria-label", "Expand this section");
  }
}

// action for collapsible definition lists
export function collapsible() {
  // clicking on the <dt> expands the section
  document.querySelectorAll(".accordion").forEach((acc) => {
    acc.onclick = (event) => {
      collapse(event.target);
    };
  });

  // clicking on the `expand-more` button expands the section
  document.querySelectorAll(".accordion .expand-more").forEach((btn) => {
    btn.onclick = (event) => {
      collapse(event.target.parentNode);
    };
  });
}
