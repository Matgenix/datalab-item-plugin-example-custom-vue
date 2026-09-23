"""A ``MixedSolution`` custom item type registered via this package's
``pydatalab.item_types`` entry point, rendered with a custom Vue panel.

It is blended from ``example-solutions`` items — the type provided by the
companion plugin `datalab-item-plugin-example` — so both plugins should be
installed together. The panel (``webapp/MixedSolutionPanel.vue``) pulls each
linked solution's concentration and computes the resulting per-solute
concentrations and total volume.

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
    """A volume of one ``example-solutions`` item taken into a :class:`MixedSolution`."""

    solution: EntryReference | None = None
    volume: float | None = None
    """Volume taken, in mL."""


class MixedSolution(Sample):
    """A solution blended from one or more ``example-solutions`` items by volume."""

    model_config = ConfigDict(
        title="Mixed Solution", json_schema_extra={"datalab_ui_color": "#b5651d"}
    )

    # The complete canonical type identifier has the form `<namespace>-<type-name>`.
    type: Literal["example-mixed-solutions"] = "example-mixed-solutions"  # type: ignore[assignment]

    components: list[MixtureComponent] = Field(default_factory=list)
