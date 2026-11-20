/*
 * Minimal Algolia search palette. Talks to the Algolia REST API directly,
 * so no DocSearch bundle is needed. Config comes from `window.SEARCH_CONFIG`.
 */
(() => {
	const cfg = window.SEARCH_CONFIG;
	if (!cfg) return;

	const HL_OPEN = "\uE000";
	const HL_CLOSE = "\uE001";
	const MAX_HITS = 12;
	const DEBOUNCE_MS = 120;
	const endpoint = `https://${cfg.appId}-dsn.algolia.net/1/indexes/${encodeURIComponent(cfg.indexName)}/query`;

	const ICONS = {
		page: '<path d="M5 2.5h6.5L16 7v10.5H5zM11 2.5V7h5M8 11h5M8 14h5"/>',
		heading: '<path d="M8 3L6.5 17M13.5 3L12 17M4 7.5h13M3 12.5h13"/>',
		para: '<path d="M4 5h12M4 9h12M4 13h12M4 17h7"/>',
	};
	const icon = (k) =>
		`<svg class="s-kind" viewBox="0 0 20 20" aria-hidden="true">${ICONS[k]}</svg>`;

	const esc = (s) =>
		s.replace(/[&<>"']/g, (c) => `&#${c.charCodeAt(0)};`);
	const mark = (s) =>
		esc(s)
			.replaceAll(HL_OPEN, "<mark>")
			.replaceAll(HL_CLOSE, "</mark>");
	const plain = (s) => s.replaceAll(HL_OPEN, "").replaceAll(HL_CLOSE, "");

	// --- DOM -----------------------------------------------------------
	// Algolia logo, taken from the DocSearch bundle.
	const ALGOLIA_LOGO = `<svg class="s-logo" viewBox="0 0 2196.2 500" role="img" aria-label="Algolia" fill="currentColor" fill-rule="evenodd"><path d="M1070.38,275.3V5.91c0-3.63-3.24-6.39-6.82-5.83l-50.46,7.94c-2.87,.45-4.99,2.93-4.99,5.84l.17,273.22c0,12.92,0,92.7,95.97,95.49,3.33,.1,6.09-2.58,6.09-5.91v-40.78c0-2.96-2.19-5.51-5.12-5.84-34.85-4.01-34.85-47.57-34.85-54.72Z"/><rect x="1845.88" y="104.73" width="62.58" height="277.9" rx="5.9" ry="5.9"/><path d="M1851.78,71.38h50.77c3.26,0,5.9-2.64,5.9-5.9V5.9c0-3.62-3.24-6.39-6.82-5.83l-50.77,7.95c-2.87,.45-4.99,2.92-4.99,5.83v51.62c0,3.26,2.64,5.9,5.9,5.9Z"/><path d="M1764.03,275.3V5.91c0-3.63-3.24-6.39-6.82-5.83l-50.46,7.94c-2.87,.45-4.99,2.93-4.99,5.84l.17,273.22c0,12.92,0,92.7,95.97,95.49,3.33,.1,6.09-2.58,6.09-5.91v-40.78c0-2.96-2.19-5.51-5.12-5.84-34.85-4.01-34.85-47.57-34.85-54.72Z"/><path d="M1631.95,142.72c-11.14-12.25-24.83-21.65-40.78-28.31-15.92-6.53-33.26-9.85-52.07-9.85-18.78,0-36.15,3.17-51.92,9.85-15.59,6.66-29.29,16.05-40.76,28.31-11.47,12.23-20.38,26.87-26.76,44.03-6.38,17.17-9.24,37.37-9.24,58.36,0,20.99,3.19,36.87,9.55,54.21,6.38,17.32,15.14,32.11,26.45,44.36,11.29,12.23,24.83,21.62,40.6,28.46,15.77,6.83,40.12,10.33,52.4,10.48,12.25,0,36.78-3.82,52.7-10.48,15.92-6.68,29.46-16.23,40.78-28.46,11.29-12.25,20.05-27.04,26.25-44.36,6.22-17.34,9.24-33.22,9.24-54.21,0-20.99-3.34-41.19-10.03-58.36-6.38-17.17-15.14-31.8-26.43-44.03Zm-44.43,163.75c-11.47,15.75-27.56,23.7-48.09,23.7-20.55,0-36.63-7.8-48.1-23.7-11.47-15.75-17.21-34.01-17.21-61.2,0-26.89,5.59-49.14,17.06-64.87,11.45-15.75,27.54-23.52,48.07-23.52,20.55,0,36.63,7.78,48.09,23.52,11.47,15.57,17.36,37.98,17.36,64.87,0,27.19-5.72,45.3-17.19,61.2Z"/><path d="M894.42,104.73h-49.33c-48.36,0-90.91,25.48-115.75,64.1-14.52,22.58-22.99,49.63-22.99,78.73,0,44.89,20.13,84.92,51.59,111.1,2.93,2.6,6.05,4.98,9.31,7.14,12.86,8.49,28.11,13.47,44.52,13.47,1.23,0,2.46-.03,3.68-.09,.36-.02,.71-.05,1.07-.07,.87-.05,1.75-.11,2.62-.2,.34-.03,.68-.08,1.02-.12,.91-.1,1.82-.21,2.73-.34,.21-.03,.42-.07,.63-.1,32.89-5.07,61.56-30.82,70.9-62.81v57.83c0,3.26,2.64,5.9,5.9,5.9h50.42c3.26,0,5.9-2.64,5.9-5.9V110.63c0-3.26-2.64-5.9-5.9-5.9h-56.32Zm0,206.92c-12.2,10.16-27.97,13.98-44.84,15.12-.16,.01-.33,.03-.49,.04-1.12,.07-2.24,.1-3.36,.1-42.24,0-77.12-35.89-77.12-79.37,0-10.25,1.96-20.01,5.42-28.98,11.22-29.12,38.77-49.74,71.06-49.74h49.33v142.83Z"/><path d="M2133.97,104.73h-49.33c-48.36,0-90.91,25.48-115.75,64.1-14.52,22.58-22.99,49.63-22.99,78.73,0,44.89,20.13,84.92,51.59,111.1,2.93,2.6,6.05,4.98,9.31,7.14,12.86,8.49,28.11,13.47,44.52,13.47,1.23,0,2.46-.03,3.68-.09,.36-.02,.71-.05,1.07-.07,.87-.05,1.75-.11,2.62-.2,.34-.03,.68-.08,1.02-.12,.91-.1,1.82-.21,2.73-.34,.21-.03,.42-.07,.63-.1,32.89-5.07,61.56-30.82,70.9-62.81v57.83c0,3.26,2.64,5.9,5.9,5.9h50.42c3.26,0,5.9-2.64,5.9-5.9V110.63c0-3.26-2.64-5.9-5.9-5.9h-56.32Zm0,206.92c-12.2,10.16-27.97,13.98-44.84,15.12-.16,.01-.33,.03-.49,.04-1.12,.07-2.24,.1-3.36,.1-42.24,0-77.12-35.89-77.12-79.37,0-10.25,1.96-20.01,5.42-28.98,11.22-29.12,38.77-49.74,71.06-49.74h49.33v142.83Z"/><path d="M1314.05,104.73h-49.33c-48.36,0-90.91,25.48-115.75,64.1-11.79,18.34-19.6,39.64-22.11,62.59-.58,5.3-.88,10.68-.88,16.14s.31,11.15,.93,16.59c4.28,38.09,23.14,71.61,50.66,94.52,2.93,2.6,6.05,4.98,9.31,7.14,12.86,8.49,28.11,13.47,44.52,13.47h0c17.99,0,34.61-5.93,48.16-15.97,16.29-11.58,28.88-28.54,34.48-47.75v50.26h-.11v11.08c0,21.84-5.71,38.27-17.34,49.36-11.61,11.08-31.04,16.63-58.25,16.63-11.12,0-28.79-.59-46.6-2.41-2.83-.29-5.46,1.5-6.27,4.22l-12.78,43.11c-1.02,3.46,1.27,7.02,4.83,7.53,21.52,3.08,42.52,4.68,54.65,4.68,48.91,0,85.16-10.75,108.89-32.21,21.48-19.41,33.15-48.89,35.2-88.52V110.63c0-3.26-2.64-5.9-5.9-5.9h-56.32Zm0,64.1s.65,139.13,0,143.36c-12.08,9.77-27.11,13.59-43.49,14.7-.16,.01-.33,.03-.49,.04-1.12,.07-2.24,.1-3.36,.1-1.32,0-2.63-.03-3.94-.1-40.41-2.11-74.52-37.26-74.52-79.38,0-10.25,1.96-20.01,5.42-28.98,11.22-29.12,38.77-49.74,71.06-49.74h49.33Z"/><path d="M249.83,0C113.3,0,2,110.09,.03,246.16c-2,138.19,110.12,252.7,248.33,253.5,42.68,.25,83.79-10.19,120.3-30.03,3.56-1.93,4.11-6.83,1.08-9.51l-23.38-20.72c-4.75-4.21-11.51-5.4-17.36-2.92-25.48,10.84-53.17,16.38-81.71,16.03-111.68-1.37-201.91-94.29-200.13-205.96,1.76-110.26,92-199.41,202.67-199.41h202.69V407.41l-115-102.18c-3.72-3.31-9.42-2.66-12.42,1.31-18.46,24.44-48.53,39.64-81.93,37.34-46.33-3.2-83.87-40.5-87.34-86.81-4.15-55.24,39.63-101.52,94-101.52,49.18,0,89.68,37.85,93.91,85.95,.38,4.28,2.31,8.27,5.52,11.12l29.95,26.55c3.4,3.01,8.79,1.17,9.63-3.3,2.16-11.55,2.92-23.58,2.07-35.92-4.82-70.34-61.8-126.93-132.17-131.26-80.68-4.97-148.13,58.14-150.27,137.25-2.09,77.1,61.08,143.56,138.19,145.26,32.19,.71,62.03-9.41,86.14-26.95l150.26,133.2c6.44,5.71,16.61,1.14,16.61-7.47V9.48C499.66,4.25,495.42,0,490.18,0H249.83Z"/></svg>`;

	const dialog = document.createElement("dialog");
	dialog.id = "search-dialog";
	dialog.setAttribute("aria-label", "Search");
	dialog.innerHTML = `
		<form method="dialog" role="search" class="s-form">
			<svg class="s-icon" viewBox="0 0 20 20" aria-hidden="true"><path d="M14 14l4 4M8.5 15a6.5 6.5 0 110-13 6.5 6.5 0 010 13z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
			<input class="s-input" type="search" autocomplete="off" autocapitalize="off"
				spellcheck="false" placeholder="${esc(cfg.placeholder)}" aria-label="Search"
				role="combobox" aria-expanded="true" aria-controls="s-list" aria-autocomplete="list">
			<kbd class="s-kbd">esc</kbd>
		</form>
		<ul class="s-list" id="s-list" role="listbox"></ul>
		<p class="s-status" aria-live="polite"></p>
		<footer class="s-foot">
			<span><kbd>↑</kbd><kbd>↓</kbd> navigate</span>
			<span><kbd>↵</kbd> open</span>
			<a href="https://www.algolia.com/ref/docsearch/?utm_source=sphinxawesome-theme&utm_medium=referral&utm_campaign=docsearch" rel="noopener nofollow" target="_blank">Powered by ${ALGOLIA_LOGO}</a>
		</footer>`;
	document.body.append(dialog);

	const input = dialog.querySelector(".s-input");
	const list = dialog.querySelector(".s-list");
	const status = dialog.querySelector(".s-status");
	let active = -1;
	let controller = null;
	let timer = 0;

	// --- Rendering -----------------------------------------------------
	/** Collapse raw records into one row per anchor, best-ranked first. */
	function toRows(hits) {
		const seen = new Set();
		const rows = [];
		for (const h of hits) {
			const levels = Object.keys(h.hierarchy)
				.filter((k) => h.hierarchy[k])
				.sort();
			const crumbs = levels.map((k) => ({
				text: h.hierarchy[k],
				html: h._highlightResult?.hierarchy?.[k]?.value ?? h.hierarchy[k],
			}));
			const isContent = h.type === "content";
			const title = crumbs.at(-1);
			const trail = crumbs.slice(0, -1).map((c) => c.text);
			const key = `${h.url}|${isContent ? h.content?.slice(0, 40) : ""}`;
			if (seen.has(key)) continue;
			seen.add(key);
			rows.push({
				url: h.url,
				title: title.html,
				trail: plain(trail.join(" › ")),
				kind: isContent ? "para" : h.type === "lvl1" ? "page" : "heading",
				snippet: isContent ? h._snippetResult?.content?.value : null,
			});
		}
		return rows;
	}

	function render(rows, query) {
		active = -1;
		input.removeAttribute("aria-activedescendant");
		status.textContent = "";
		list.innerHTML = rows
			.map(
				(r, i) => `
			<li role="option" id="s-opt-${i}">
				<a href="${esc(r.url)}" tabindex="-1">
					${icon(r.kind)}
					<span class="s-body">
						${r.trail ? `<span class="s-trail">${esc(r.trail)}</span>` : ""}
						<span class="s-title">${mark(r.title)}</span>
						${r.snippet ? `<span class="s-snip">${mark(r.snippet)}</span>` : ""}
					</span>
				</a>
			</li>`,
			)
			.join("");
		if (!rows.length && query) {
			const url = cfg.missingResultsUrl?.replace("${query}", encodeURIComponent(query));
			status.innerHTML =
				`No results for “${esc(query)}”.` +
				(url ? ` <a href="${esc(url)}" rel="noopener nofollow" target="_blank">Report missing results</a>` : "");
		}
		if (rows.length) select(0);
	}

	function select(i) {
		const items = list.children;
		if (!items.length) return;
		active = (i + items.length) % items.length;
		for (const [n, el] of [...items].entries()) {
			el.setAttribute("aria-selected", String(n === active));
		}
		input.setAttribute("aria-activedescendant", `s-opt-${active}`);
		items[active].scrollIntoView({ block: "nearest" });
	}

	// --- Querying ------------------------------------------------------
	async function search(query) {
		controller?.abort();
		if (!query.trim()) return render([], "");
		controller = new AbortController();
		try {
			const res = await fetch(endpoint, {
				method: "POST",
				signal: controller.signal,
				// text/plain avoids a CORS preflight, as recommended by Algolia.
				headers: {
					"Content-Type": "text/plain",
					"X-Algolia-Application-Id": cfg.appId,
					"X-Algolia-API-Key": cfg.apiKey,
				},
				body: JSON.stringify({
					query,
					hitsPerPage: MAX_HITS * 2,
					attributesToRetrieve: ["hierarchy", "url", "type", "content"],
					attributesToHighlight: ["hierarchy"],
					attributesToSnippet: ["content:12"],
					highlightPreTag: HL_OPEN,
					highlightPostTag: HL_CLOSE,
					snippetEllipsisText: "…",
					...cfg.searchParameters,
				}),
			});
			if (!res.ok) throw new Error(res.statusText);
			const { hits } = await res.json();
			render(toRows(hits).slice(0, MAX_HITS), query);
		} catch (err) {
			if (err.name === "AbortError") return;
			list.innerHTML = "";
			status.textContent = "Search is unavailable right now.";
		}
	}

	// --- Events --------------------------------------------------------
	input.addEventListener("input", () => {
		clearTimeout(timer);
		timer = setTimeout(() => search(input.value), DEBOUNCE_MS);
	});

	input.addEventListener("keydown", (e) => {
		if (e.key === "ArrowDown") select(active + 1);
		else if (e.key === "ArrowUp") select(active - 1);
		else if (e.key === "Enter") {
			const a = list.children[active]?.querySelector("a");
			if (!a) return;
			e.preventDefault();
			if (e.metaKey || e.ctrlKey) window.open(a.href, "_blank", "noopener");
			else window.location.assign(a.href);
		} else return;
		e.preventDefault();
	});

	list.addEventListener("mousemove", (e) => {
		const li = e.target.closest("li");
		if (li) select([...list.children].indexOf(li));
	});
	list.addEventListener("click", () => dialog.close());

	// Close on backdrop click.
	dialog.addEventListener("mousedown", (e) => {
		if (e.target === dialog) dialog.close();
	});

	const open = () => {
		if (!dialog.open) dialog.showModal();
		input.select();
	};

	document.addEventListener("keydown", (e) => {
		const typing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName) ||
			document.activeElement?.isContentEditable;
		if ((e.key === "k" && (e.metaKey || e.ctrlKey)) || (e.key === "/" && !typing)) {
			e.preventDefault();
			open();
		}
	});

	for (const el of document.querySelectorAll("[data-search-open]")) {
		el.addEventListener("click", open);
	}
})();
