// collapsible definition lists
import { Controller } from "stimulus"

export default class extends Controller {

  // clicking on the `dt.accordion` expands the section
  expandAccordion(event) {
    this.expand(event.target)
  }

  // clicking on the `expand-more` button expands the section
  expandMore(event) {
    this.expand(event.target.parentNode)
  }

  expand(element) {
    // element should be the `dt.accordion`
    element.classList.toggle('active')
    const btn = element.querySelector('button.expand-more')

    if (element.classList.contains("active")) {
      btn.setAttribute("aria-expanded", "true")
      btn.setAttribute("aria-label", "Collapse this section")
    } else {
      btn.setAttribute("aria-expanded", "false")
      btn.setAttribute("aria-label", "Expand this section")
    }
  }
}
