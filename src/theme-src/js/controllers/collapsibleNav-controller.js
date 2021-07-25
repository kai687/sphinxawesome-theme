// collapse / expand the navigation sections in the side bar

import { Controller } from "stimulus"

export default class extends Controller {

  expand(event) {
    const icon = event.currentTarget
    icon.parentElement.parentElement.classList.toggle("expanded")
  }

  expandOnFocus(event) {
    const focusedLink = event.target
    focusedLink

    // this behavior should change.
    // keyboard focus should only be possible if the links are visible
    // should I use tabIndex here?
  }
}
