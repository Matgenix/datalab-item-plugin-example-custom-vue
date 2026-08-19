"""A ``MixedSolution`` custom item type registered via this package's
``pydatalab.item_types`` entry point, rendered with a custom Vue panel.

It is blended from ``solutions`` items — the type provided by the companion
plugin `datalab-item-plugin-example` — so both plugins should be installed
together. The panel (``webapp/MixedSolutionPanel.vue``) pulls each linked
solution's concentration and computes the resulting per-solute concentrations
and total volume.

Because this plugin ships a custom panel, the panel is responsible for
rendering ALL of this model's custom fields (datalab does not render the
leftover fields for you). The ``datalab_*`` schema hints still control summary
projection and API-side validation.
"""

from typing import Literal

from pydantic import ConfigDict, Field
from pydatalab.models.samples import Sample
from pydatalab.models.utils import BaseModel, EntryReference


class MixtureComponent(BaseModel):
    """A volume of one ``solutions`` item taken into a :class:`MixedSolution`."""

    solution: EntryReference | None = None
    volume: float | None = None
    """Volume taken, in mL."""


class MixedSolution(Sample):
    """A solution blended from one or more ``solutions`` items by volume."""

    model_config = ConfigDict(
        title="Mixed Solution", json_schema_extra={"datalab_ui_color": "#b5651d"}
    )

    # The unique type identifier for this model; it must not collide with a
    # built-in type (samples, cells, starting_materials, equipment) or another plugin.
    type: Literal["mixed_solutions"] = "mixed_solutions"  # type: ignore[assignment]

    components: list[MixtureComponent] = Field(default_factory=list)
