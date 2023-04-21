window.addEventListener("DOMContentLoaded", () => {
  document
    .getElementById("upvote")
    .addEventListener("click", () => sendEvent("upvote"))

  document
    .getElementById("downvote")
    .addEventListener("click", () => sendEvent("downvote"))

  document
    .querySelectorAll("button.copy")
    .forEach((i) => {
      i.addEventListener("click", () => sendEvent("code copied"))
    })

  document
    .querySelector("button.DocSearch-Button")
    .addEventListener("click", () => sendEvent("search clicked"))
})

function sendEvent(eventType) {
  if (window.umami) {
    umami.track(eventType)
  } else {
    console.log(`Simulating: ${eventType}`)
  }
}
