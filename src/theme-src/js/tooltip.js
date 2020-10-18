function showTooltip(event, text) {
  const rect = event.target.getBoundingClientRect();
  const tooltip = document.querySelector("#tooltip");

  tooltip.style.opacity = 0.6;
  tooltip.style.visibility = "visible";
  tooltip.style.top = rect.y + rect.height + 1 + "px";
  tooltip.style.left = rect.x - 4 + "px";
  tooltip.textContent = text;
}

function hideTooltip() {
  const tooltip = document.querySelector("#tooltip");

  tooltip.textContent = "";
  tooltip.style.opacity = 0;
  tooltip.style.visibility = "hidden";
}

function tooltipEvents() {
  const tooltip = document.querySelector("#tooltip");
  // hide 'copied' tooltip on scroll
  window.onscroll = () => {
    tooltip.textContent = "";
    tooltip.style.opacity = 0;
    tooltip.style.visibility = "hidden";
  };
}

export { showTooltip, hideTooltip, tooltipEvents };
