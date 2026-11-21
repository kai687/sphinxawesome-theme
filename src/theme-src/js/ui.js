/** Small UI behaviors. Initial dark mode is set by an inline script in `layout.html`. */

const DARK_KEY = "_x_darkMode";

function store(key, value) {
	try {
		localStorage.setItem(key, value);
	} catch {
		// Storage can be unavailable (private mode); ignore.
	}
}

/** Toggle the color scheme and remember the choice. */
export function initThemeToggle() {
	const root = document.documentElement;
	for (const button of document.querySelectorAll("[data-theme-toggle]")) {
		button.addEventListener("click", () => {
			store(DARK_KEY, root.classList.toggle("dark"));
		});
	}
}

/** Open and close the mobile sidebar. */
export function initSidebar() {
	const sidebar = document.getElementById("left-sidebar");
	const backdrop = document.getElementById("sidebar-backdrop");
	if (!sidebar) {
		return;
	}

	// Below the `md` breakpoint the sidebar is an off-canvas drawer. While it is
	// closed, `inert` keeps its links out of the tab order and the accessibility tree.
	const desktop = window.matchMedia("(min-width: 768px)");
	let open = false;

	const render = () => {
		sidebar.classList.toggle("translate-x-0", open);
		sidebar.inert = !open && !desktop.matches;
		document.body.classList.toggle("overflow-hidden", open);
		if (backdrop) {
			backdrop.hidden = !open;
		}
	};
	const setOpen = (value) => {
		open = value;
		render();
	};
	desktop.addEventListener("change", () => {
		// Leaving the drawer layout closes it, so the page can scroll again.
		if (desktop.matches) {
			open = false;
		}
		render();
	});
	render();

	for (const button of document.querySelectorAll("[data-sidebar-open]")) {
		button.addEventListener("click", () => setOpen(true));
	}
	for (const button of document.querySelectorAll("[data-sidebar-close]")) {
		button.addEventListener("click", () => setOpen(false));
	}
	backdrop?.addEventListener("click", (event) => {
		if (event.target === backdrop) {
			setOpen(false);
		}
	});
}

/** Expand and collapse navigation entries that have children. */
export function initCollapsibleNav() {
	const sidebar = document.getElementById("left-sidebar");
	if (!sidebar) {
		return;
	}

	sidebar.addEventListener("click", (event) => {
		const link = event.target.closest("a.expandable");
		if (!link || !sidebar.contains(link)) {
			return;
		}
		const children = link.nextElementSibling;
		if (children?.tagName !== "UL") {
			return;
		}
		// The chevron button only toggles; the rest of the link also navigates.
		if (event.target.closest("button")) {
			event.preventDefault();
			event.stopPropagation();
		}
		children.hidden = !children.hidden;
		link.classList.toggle("expanded", !children.hidden);
	});
}

/** Copy the URL of a header link on click. */
export function initHeaderlinks() {
	for (const link of document.querySelectorAll("a.headerlink")) {
		link.addEventListener("click", (event) => {
			event.preventDefault();
			navigator.clipboard?.writeText(link.href);
			link.setAttribute("data-tooltip", "Copied!");
			setTimeout(() => {
				link.setAttribute("data-tooltip", "Copy link to this element");
			}, 2000);
		});
	}
}

/** Mark the on-page TOC link of the section in view. */
export function initScrollspy() {
	const targets = document.querySelectorAll("a.headerlink[data-scrollspy]");
	const tocLinks = document.querySelectorAll("#right-sidebar a");
	if (!targets.length || !tocLinks.length) {
		return;
	}

	const observer = new IntersectionObserver(
		(entries) => {
			for (const entry of entries) {
				if (!entry.isIntersecting) {
					continue;
				}
				const active = entry.target.getAttribute("href");
				for (const link of tocLinks) {
					link.dataset.current = String(link.getAttribute("href") === active);
				}
			}
		},
		{ rootMargin: "0% 0% -70% 0%" },
	);
	for (const target of targets) {
		observer.observe(target);
	}
}

/** Show the scroll-to-top button after scrolling down. */
export function initScrollTop() {
	const button = document.getElementById("scrolltop");
	if (!button) {
		return;
	}

	const update = () => {
		const hidden = window.scrollY <= 100;
		button.classList.toggle("opacity-0", hidden);
		button.classList.toggle("invisible", hidden);
	};
	window.addEventListener("scroll", update, { passive: true });
	update();
	button.addEventListener("click", () => {
		window.scrollTo({ top: 0, behavior: "smooth" });
	});
}

/** Focus the search input with Cmd+K or Ctrl+K. The hint shows the platform's modifier. */
export function initSearchShortcut() {
	const input = document.getElementById("search-input");
	if (!input) {
		return;
	}

	const platform =
		navigator.userAgentData?.platform || navigator.platform || "";
	const isApple = /mac|iphone|ipad/i.test(platform);
	if (!isApple) {
		for (const key of document.querySelectorAll("[data-modifier-key]")) {
			key.textContent = "Ctrl";
		}
	}

	window.addEventListener("keydown", (event) => {
		if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
			event.preventDefault();
			input.focus();
		}
	});
}
