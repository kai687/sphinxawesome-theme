// action for collapsible definition lists
export function collapsible() {
  document.querySelectorAll(".accordion").forEach((acc) => {
    acc.onclick = (event) => {
      event.target.classList.toggle("active");
    };
  });
}
