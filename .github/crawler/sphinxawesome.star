# Extract records from https://sphinxawesome.xyz for the custom search in docs/_static/search.js.
# Records only contain the fields used by the search UI and the index settings,
# so they aren't compatible with the DocSearch UI.

# Extractor functions only differ in the section (lvl0).
def handle_how_to(pattern, doc, ctx):
    return docsearch_records(doc, ctx, "How To")

def handle_demo(pattern, doc, ctx):
    return docsearch_records(doc, ctx, "Demo")

def handle_about(pattern, doc, ctx):
    return docsearch_records(doc, ctx, "About")

def handle_changelog(pattern, doc, ctx):
    return docsearch_records(doc, ctx, "Changelog")

def handle_api(pattern, doc, ctx):
    return docsearch_records(doc, ctx, "API")

def handle_home(pattern, doc, ctx):
    return docsearch_records(doc, ctx, "Get started")

# Register extraction functions. Order matters.
extract("^/how-to/", handle_how_to)
extract("^/demo/", handle_demo)
extract("^/about/$", handle_about)
extract("^/changelog/$", handle_changelog)
extract("^/autoapi/", handle_api)
extract("^/$", handle_home)


def docsearch_records(doc, ctx, lvl0):
    """Build the records for a page: one per heading and one per section content."""
    # Only index content that's a child of `#content`.
    root = doc.select_first("#content")
    if root == None:
        return []

    heading_records = []
    content_records = []
    hierarchy = {"lvl0": lvl0}
    position = 0
    # Store the path only, so links work on any host (local builds, previews).
    base_url = "/" + url_without_anchor(ctx["url"]).split("/", 3)[3]

    # In Sphinx, sections have the IDs, not the headings.
    for section in root.select("section[id]"):
        # Index only up to h4.
        heading = section.select_first("h1, h2, h3, h4")
        if heading == None:
            title = ""
        else:
            title = escape_html(collapse_space(text(heading)))
        if title == "":
            continue

        name = node_name(heading)
        if name == "h1":
            level = 1
        elif name == "h2":
            level = 2
        elif name == "h3":
            level = 3
        elif name == "h4":
            level = 4
        else:
            continue

        hierarchy["lvl" + str(level)] = title

        # Reset lower levels when setting a new higher level.
        for child in [2, 3, 4, 5, 6]:
            if child > level:
                key = "lvl" + str(child)
                if key in hierarchy:
                    hierarchy.pop(key)

        # Set the anchor based on the section ID.
        anchor = attr(section, "id")
        if anchor == None:
            anchor = ""
        else:
            anchor = collapse_space(anchor)

        if anchor == "":
            record_url = base_url
        else:
            record_url = base_url + "#" + anchor

        # Only include the levels that are set.
        record_hierarchy = {}
        for key in ["lvl0", "lvl1", "lvl2", "lvl3", "lvl4"]:
            if key in hierarchy:
                record_hierarchy[key] = hierarchy[key]

        heading_records.append(docsearch_record(
            position,
            "lvl" + str(level),
            record_hierarchy,
            None,
            record_url,
            base_url,
            100 - (level * 10),
        ))
        position += 1

        # Index content from `p` and `li`.
        # Sphinx nests sections, so `section.select("p, li")` would also grab
        # subsection content. Direct-child selectors would miss wrapped content
        # such as lists/admonitions. Build a selector for deeper nested sections
        # and skip nodes that belong to those subsections.
        parts = []
        nested_section_parts = []
        for i in range(level + 1):
            nested_section_parts.append("section")
        nested_section_selector = " ".join(nested_section_parts)

        for node in section.select("p, li"):
            if nested_section_selector != "" and has_parent(node, nested_section_selector):
                continue
            value = escape_html(trim(text(node)))
            if value != "":
                parts.append(value)
        content = "\r\n".join(parts)
        if content != "":
            content_records.append(docsearch_record(
                position,
                "content",
                record_hierarchy,
                content,
                record_url,
                base_url,
                0,
            ))
            position += 1

    return heading_records + content_records


def docsearch_record(position, record_type, hierarchy, content, url, base_url, level_weight):
    """Return a search record.

    `weight.level` ranks headings above content, `weight.position` keeps page order.
    """
    record = {
        "objectID": str(position) + "-" + base_url,
        "type": record_type,
        "hierarchy": hierarchy,
        "url": url,
        "weight": {
            "level": level_weight,
            "position": position,
        },
    }
    if content != None:
        record["content"] = content
    return record
