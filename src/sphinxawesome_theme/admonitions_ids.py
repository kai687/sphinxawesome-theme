"""Add ids to all admonition nodes.

So that admonitions also can have permalinks.

:copyright: Copyright 2020, Kai Welke.
:license: MIT, see LICENSE.
"""

from typing import Any

from docutils import nodes
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging

logger = logging.getLogger(__name__)


class AdmonitionId(SphinxPostTransform):
    """traverse all admonition nodes and add IDs."""

    default_priority = 10

    def run(self, **kwargs: Any) -> None:
        """Run the AdmonitionID posttransform."""
        note_id = 1
        for node in self.document.traverse():
            if isinstance(node, nodes.section):
                if node["names"]:
                    title = nodes.make_id(node["names"][0])
                elif self.document.nameids:
                    title = nodes.make_id(list(self.document.nameids)[0])
                else:
                    title = "unknown"

            if isinstance(node, nodes.Admonition):
                node["ids"] = [f"{title}-note-{note_id}"]
                note_id += 1
