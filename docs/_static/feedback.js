window.addEventListener("DOMContentLoaded", () => {
  const upvote = document.getElementById("upvote")
  if (upvote) {
    upvote.addEventListener("click", () => sendEvent("upvote"))
  }

  const downvote = document.getElementById("downvote")
  if (downvote) {
    downvote.addEventListener("click", () => sendEvent("downvote"))
  }

  const copy = document.querySelectorAll("button.copy")
  if (copy) {
    copy.forEach((i) => {
      i.addEventListener("click", () => sendEvent("code copied"))
    })
  }

  const docsearch = document.querySelector("button.DocSearch-Button")
  if (docsearch) {
    docsearch.addEventListener("click", () => sendEvent("search clicked"))
  }
})

function sendEvent(eventType) {
  if (window.umami) {
    umami.track(eventType)
  } else {
    console.log(`Simulating: ${eventType}`)
  }
}
