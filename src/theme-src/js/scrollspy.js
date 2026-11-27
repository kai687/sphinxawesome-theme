/**
 * Highlight the current section in the on-page TOC.
 *
 * The postprocessing step marks each heading's permalink with
 * `data-scrollspy`. The current section is the last heading that has
 * scrolled above a line near the top of the viewport. At the very bottom
 * of the page, the last heading wins, so short final sections can still
 * become active even though the page can't scroll any further.
 */
export function initScrollspy() {
	const links = [...document.querySelectorAll("a.headerlink[data-scrollspy]")];
	if (links.length === 0) {
		return;
	}

	const root = document.documentElement;
	let ticking = false;
	let current;

	function findCurrent() {
		const atBottom =
			window.innerHeight + window.scrollY >=
			document.documentElement.scrollHeight - 2;
		if (atBottom) {
			return links[links.length - 1].getAttribute("href");
		}
		const line = window.innerHeight * 0.3;
		let active = "";
		for (const link of links) {
			if (link.getBoundingClientRect().top > line) {
				break;
			}
			active = link.getAttribute("href");
		}
		return active;
	}

	function update() {
		ticking = false;
		const next = findCurrent();
		if (next === current) {
			return;
		}
		current = next;
		// The root element's Alpine state holds `activeSection`.
		const data = window.Alpine?.$data(root);
		if (data) {
			data.activeSection = next;
		}
	}

	function requestUpdate() {
		if (!ticking) {
			ticking = true;
			window.requestAnimationFrame(update);
		}
	}

	window.addEventListener("scroll", requestUpdate, { passive: true });
	window.addEventListener("resize", requestUpdate);
	requestUpdate();
}
