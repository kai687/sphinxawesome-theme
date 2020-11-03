"""Add ids to all admonition nodes.

This allows admonitions, such as notes, warnings, etc.
to also be linked to.

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE.
"""

from typing import Any, Dict

from docutils import nodes
from sphinx.addnodes import desc
from sphinx.application import Sphinx
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging

from . import __version__

logger = logging.getLogger(__name__)


class AdmonitionId(SphinxPostTransform):
    """Add IDs to admonition nodes.

    This SphinxPostTransform is executed for "html"
    and "dirhtml" builders, so that permalinks
    can be added to the node titles.
    """

    default_priority = 10
    # this postransform should only be applied for the HTML builders
    builders = ("html", "dirhtml")

    def run(self, **kwargs: Any) -> None:
        """Run the post-transform.

        Iterate over all nodes. If the node is a ``section`` node,
        obtain the title from the names field.
        If the node is an admonition (but not a ``desc`` node),
        assign an ID of the form ``<sectiontitle>-note-<#>``.
        """
        note_id = 1
        title = "undefined"
        for node in self.document.traverse():
            if isinstance(node, nodes.section):
                if node["names"]:  # pragma: nocover
                    title = nodes.make_id(node["names"][0])

            # <desc> nodes are also admonitions for some reason
            if isinstance(node, nodes.Admonition) and not isinstance(node, desc):
                node["ids"] = [f"{title}-note-{note_id}"]
                note_id += 1


def setup(app: Sphinx) -> Dict[str, Any]:
    """Register this post-transform as extension."""
    app.add_post_transform(AdmonitionId)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
