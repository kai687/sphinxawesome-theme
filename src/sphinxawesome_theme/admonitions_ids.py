"""Add ids to all admonition nodes.

So that admonitions also can have permalinks.

:copyright: Copyright 2020, Kai Welke.
:license: MIT, see LICENSE.
"""

from typing import Any

from docutils import nodes
from sphinx.addnodes import desc
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging

logger = logging.getLogger(__name__)


class AdmonitionId(SphinxPostTransform):
    """Traverse all admonition nodes and add IDs."""

    default_priority = 10
    # this postransform should only be applied for the HTML builders
    builders = ("html", "dirhtml")

    def run(self, **kwargs: Any) -> None:
        """Run the AdmonitionID posttransform."""
        note_id = 1
        for node in self.document.traverse():
            if isinstance(node, nodes.section):
                if node["names"]:
                    title = nodes.make_id(node["names"][0])
                else:
                    title = "unknown"

            # <desc> nodes are also admonitions for some reason
            if isinstance(node, nodes.Admonition) and not isinstance(node, desc):
                node["ids"] = [f"{title}-note-{note_id}"]
                note_id += 1
