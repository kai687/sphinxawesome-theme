document
  .getElementById("upvote")
  .addEventListener("click", () => vote("upvote"))

document
  .getElementById("downvote")
  .addEventListener("click", () => vote("downvote"))

function vote(eventType) {
  if (window.umami) {
    umami.track(eventType)
  } else {
    console.log(`Simulating: ${eventType}`)
  }
}
