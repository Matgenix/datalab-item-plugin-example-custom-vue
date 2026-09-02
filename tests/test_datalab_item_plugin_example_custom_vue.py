from importlib.metadata import entry_points
from pathlib import Path

from datalab_item_plugin_example_custom_vue import __version__
from datalab_item_plugin_example_custom_vue.models import MixedSolution


def test_version():
    assert __version__


def test_entry_point_is_registered():
    """The entry point is how datalab discovers this plugin at startup."""
    eps = [ep for ep in entry_points(group="pydatalab.item_types") if ep.name == "mixed_solutions"]
    assert len(eps) == 1
    assert eps[0].load() is MixedSolution


def test_model_registers_with_datalab():
    """Mirror what `pydatalab.apps.load_item_plugins` does at server startup;
    this also validates all `datalab_*` schema hints on the model."""
    from pydatalab.models import ITEM_MODELS, register_item_model

    register_item_model(MixedSolution)
    assert ITEM_MODELS["_mixed_solutions"] is MixedSolution


def test_model_round_trip():
    item = MixedSolution(item_id="test-item-1")
    assert item.type == "_mixed_solutions"
    assert MixedSolution(**item.model_dump()).item_id == "test-item-1"


def test_panel_follows_naming_convention():
    """`invoke dev.collect-plugin-panels` looks for `webapp/<ClassName>Panel.vue`
    inside the package directory."""
    import datalab_item_plugin_example_custom_vue

    package_dir = Path(datalab_item_plugin_example_custom_vue.__file__).parent
    assert (package_dir / "webapp" / "MixedSolutionPanel.vue").is_file()
