/* Search palette backed by the Algolia REST API. Markup lives in _templates/searchbox.html. */
(() => {
	const dialog = document.getElementById("search-dialog");
	if (!dialog) return;

	const { appId, apiKey, indexName, missingResultsUrl } = JSON.parse(dialog.dataset.config);
	const input = dialog.querySelector(".s-input");
	const list = dialog.querySelector(".s-list");
	const status = dialog.querySelector(".s-status");
	const row = document.getElementById("search-row");

	// The crawler HTML-escapes all indexed text and the index highlights matches with <mark>,
	// so Algolia's values are safe to insert as HTML.

	function render(hits, query) {
		let prevPage;
		list.replaceChildren(
			...hits.map((h) => {
				const levels = Object.keys(h.hierarchy).sort().filter((k) => h.hierarchy[k]);
				const last = levels.pop();
				const kind = h.type === "content" ? "para" : h.type === "lvl1" ? "page" : "heading";
				const li = row.content.cloneNode(true);
				const text = (sel, value) => {
					const el = li.querySelector(sel);
					if (value) el.innerHTML = value;
					else el.remove();
				};
				// Hits on the same page as the row above nest under it, without a repeated breadcrumb.
				const page = h.url.split("#")[0];
				const child = kind !== "page" && page === prevPage;
				prevPage = page;
				li.firstElementChild.classList.toggle("s-child", child);
				li.querySelector("a").href = h.url;
				li.querySelector("use").setAttribute("href", `#s-${kind}`);
				text(".s-trail", !(child && kind === "heading") && levels.map((k) => h.hierarchy[k]).join(" › "));
				text(".s-title", h._highlightResult.hierarchy[last].value);
				text(".s-snip", kind === "para" && h._snippetResult.content.value);
				return li;
			}),
		);
		status.innerHTML = "";
		if (hits.length || !query) return;
		status.textContent = `No results for “${query}”. `;
		if (missingResultsUrl) {
			const a = Object.assign(document.createElement("a"), {
				href: missingResultsUrl.replace("${query}", encodeURIComponent(query)),
				textContent: "Report missing results",
				target: "_blank",
				rel: "noopener nofollow",
			});
			status.append(a);
		}
	}

	let controller;
	let timer;
	async function search(query) {
		controller?.abort();
		if (!query.trim()) return render([], "");
		controller = new AbortController();
		try {
			const res = await fetch(`https://${appId}-dsn.algolia.net/1/indexes/${encodeURIComponent(indexName)}/query`, {
				method: "POST",
				signal: controller.signal,
				// text/plain avoids a CORS preflight, as recommended by Algolia.
				headers: { "Content-Type": "text/plain", "X-Algolia-Application-Id": appId, "X-Algolia-API-Key": apiKey },
				body: JSON.stringify({ query }),
			});
			if (!res.ok) throw new Error(res.statusText);
			render((await res.json()).hits, query);
		} catch (err) {
			if (err.name !== "AbortError") status.textContent = "Search is unavailable right now.";
		}
	}

	input.addEventListener("input", () => {
		clearTimeout(timer);
		timer = setTimeout(() => search(input.value), 120);
	});

	// Results are plain links: arrows move focus, Enter and ⌘Enter use native link behavior.
	dialog.addEventListener("keydown", (e) => {
		// In a search input, Esc first clears the field. Close right away instead.
		if (e.key === "Escape") {
			e.preventDefault();
			dialog.close();
			return;
		}
		const dir = { ArrowDown: 1, ArrowUp: -1 }[e.key];
		if (dir) {
			const links = [...list.querySelectorAll("a")];
			const next = links[links.indexOf(document.activeElement) + dir] ?? (dir < 0 ? input : null);
			e.preventDefault();
			next?.focus();
		} else if (e.key.length === 1 && !e.metaKey && !e.ctrlKey) {
			input.focus();
		}
	});
	input.form.addEventListener("submit", (e) => {
		e.preventDefault();
		list.querySelector("a")?.click();
	});
	// Same-page anchors don't reload, so close explicitly.
	list.addEventListener("click", () => dialog.close());

	// Fallbacks for browsers without invoker commands or `closedby`.
	if (!("commandForElement" in HTMLButtonElement.prototype)) {
		for (const btn of document.querySelectorAll("[commandfor=search-dialog]")) {
			btn.addEventListener("click", () => dialog.showModal());
		}
	}
	if (!("closedBy" in HTMLDialogElement.prototype)) {
		dialog.addEventListener("click", (e) => e.target === dialog && dialog.close());
	}

	document.addEventListener("keydown", (e) => {
		const typing = document.activeElement.matches("input, textarea, select, [contenteditable]");
		if ((e.key === "k" && (e.metaKey || e.ctrlKey)) || (e.key === "/" && !typing)) {
			e.preventDefault();
			dialog.showModal();
			input.select();
		}
	});
})();
