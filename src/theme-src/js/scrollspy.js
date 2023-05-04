/** Highlight active section in the TOC */
export function scrollSpy() {
  const sections = document.querySelectorAll('#content section')
  const options = {
    rootMargin: '-70px 0% -80% 0%',
  }

  const observer = new IntersectionObserver(highlightCurrentSection, options)

  sections.forEach((section) => {
    observer.observe(section)
  })
}

function highlightCurrentSection(entries) {
  entries.forEach((entry) => {
    const matchingLink = document.querySelector(
      `#right-sidebar a[href*=${entry.target.id}]`
    )

    if (entry.isIntersecting && matchingLink) {
      matchingLink.setAttribute('data-current', 'true')
    } else if (matchingLink) {
      matchingLink.removeAttribute('data-current')
    }
  })
}
