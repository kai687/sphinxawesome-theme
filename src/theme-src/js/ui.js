/**
 * Small UI behaviors for the theme: color scheme, mobile drawer,
 * collapsible navigation, permalinks, scroll-to-top and search shortcut.
 *
 * The server renders the initial state (see `postprocess.py` and the
 * templates), so these functions only react to user input.
 */

const STORAGE_KEY = "_x_darkMode";

/** Toggle the color scheme. The `dark` class on `<html>` is the source of truth. */
export function initTheme() {
	const root = document.documentElement;
	const button = document.querySelector("[data-theme-toggle]");
	if (!button) {
		return;
	}

	const sync = () =>
		button.setAttribute(
			"aria-pressed",
			String(root.classList.contains("dark")),
		);
	sync();
	// Also follows the head script, which reacts to OS preference changes.
	new MutationObserver(sync).observe(root, {
		attributes: true,
		attributeFilter: ["class"],
	});

	button.addEventListener("click", () => {
		const dark = !root.classList.contains("dark");
		root.classList.toggle("dark", dark);
		try {
			localStorage.setItem(STORAGE_KEY, String(dark));
		} catch {
			// Storage can be blocked. The choice then lasts until reload.
		}
	});
}

/**
 * The mobile drawer: open and close buttons, overlay, Escape and breakpoint.
 *
 * While the drawer is open, everything outside it is made `inert`, so focus
 * can't move to the blurred page behind it. Focus moves into the drawer on
 * open and returns to the button that opened it on close.
 */
export function initSidebar() {
	const sidebar = document.getElementById("left-sidebar");
	if (!sidebar) {
		return;
	}
	const overlay = document.getElementById("sidebar-overlay");
	const mobile = window.matchMedia("(max-width: 767px)");
	let open = false;
	let opener = null;
	let blocked = [];

	/** Make all content outside the drawer inert, or undo that. */
	function setBackgroundInert(inert) {
		if (!inert) {
			for (const element of blocked) {
				element.inert = false;
			}
			blocked = [];
			return;
		}
		let node = sidebar;
		while (node !== document.body && node.parentElement) {
			for (const sibling of node.parentElement.children) {
				const skip =
					sibling === node ||
					sibling === overlay ||
					["SCRIPT", "STYLE", "LINK"].includes(sibling.tagName);
				if (!skip && !sibling.inert) {
					sibling.inert = true;
					blocked.push(sibling);
				}
			}
			node = node.parentElement;
		}
	}

	function render() {
		const closed = mobile.matches && !open;
		sidebar.inert = closed;
		if (closed) {
			sidebar.setAttribute("aria-hidden", "true");
		} else {
			sidebar.removeAttribute("aria-hidden");
		}
		sidebar.classList.toggle("translate-x-0", open);
		document.body.classList.toggle("overflow-hidden", open);
		setBackgroundInert(open && mobile.matches);
		if (overlay) {
			overlay.hidden = !open;
		}
	}

	function setOpen(value, trigger) {
		if (value === open) {
			return;
		}
		open = value;
		render();
		if (open) {
			opener = trigger ?? document.activeElement;
			sidebar.querySelector("a[href], button")?.focus();
		} else {
			opener?.focus();
			opener = null;
		}
	}

	for (const button of document.querySelectorAll("[data-sidebar-open]")) {
		button.addEventListener("click", () => setOpen(true, button));
	}
	for (const button of document.querySelectorAll("[data-sidebar-close]")) {
		button.addEventListener("click", () => setOpen(false));
	}
	overlay?.addEventListener("click", () => setOpen(false));
	document.addEventListener("keydown", (event) => {
		if (event.key === "Escape") {
			setOpen(false);
		}
	});
	mobile.addEventListener("change", (event) => {
		if (!event.matches) {
			open = false;
			opener = null;
		}
		render();
	});
	render();
}

/** Expand and collapse navigation branches. */
export function initNav() {
	const sidebar = document.getElementById("left-sidebar");
	if (!sidebar) {
		return;
	}

	sidebar.addEventListener("click", (event) => {
		const link = event.target.closest("a.expandable");
		if (!link || !sidebar.contains(link)) {
			return;
		}
		// The chevron button only toggles. Clicking the link also navigates.
		if (event.target.closest("button")) {
			event.preventDefault();
		}
		const expanded = link.classList.toggle("expanded");
		const children = link.nextElementSibling;
		if (children) {
			children.hidden = !expanded;
		}
	});
}

/** Copy a heading's permalink instead of following it. */
export function initHeaderLinks() {
	const timers = new WeakMap();

	document.addEventListener("click", (event) => {
		const link = event.target.closest("a.headerlink[data-copy-link]");
		if (!link) {
			return;
		}
		event.preventDefault();
		navigator.clipboard?.writeText(link.href)?.catch(() => {});
		link.setAttribute("data-tooltip", "Copied!");
		clearTimeout(timers.get(link));
		timers.set(
			link,
			setTimeout(
				() => link.setAttribute("data-tooltip", "Copy link to this element"),
				2000,
			),
		);
	});
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
	button.addEventListener("click", () =>
		window.scrollTo({ top: 0, behavior: "smooth" }),
	);
	update();
}

/** Focus the search field with Cmd+K (macOS) or Ctrl+K. */
export function initSearchShortcut() {
	const input = document.getElementById("search-input");
	if (!input) {
		return;
	}

	// Show the shortcut that works on this platform.
	const platform = navigator.userAgentData?.platform ?? navigator.platform;
	if (!/mac|iphone|ipad/i.test(platform)) {
		const key = document.querySelector("#searchbox kbd span");
		if (key) {
			key.textContent = "Ctrl";
		}
	}

	document.addEventListener("keydown", (event) => {
		if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
			event.preventDefault();
			input.focus();
		}
	});
}
