function hideSnackbar() {
  const snackbar = document.querySelector("#snackbar");
  snackbar.style.opacity = 0;
  snackbar.style.transform = "translate(0,100%)";
  snackbar.classList.remove("bg-gray-200", "text-blue-700");
  snackbar.classList.add("bg-gray-900", "text-gray-100");
}

function showSnackbar(message) {
  const snackbar = document.querySelector("#snackbar");
  snackbar.textContent = message;
  snackbar.style.opacity = 1;
  snackbar.style.transform = "translate(0,0)";
  setTimeout(hideSnackbar, 2000);
}


export { showSnackbar, hideSnackbar }
