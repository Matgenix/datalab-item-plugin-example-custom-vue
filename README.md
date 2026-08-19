# <div align="center"><i>datalab-item-plugin-example-custom-vue</i></div>

<div align="center">
<a href="https://github.com/Matgenix/datalab-item-plugin-example-custom-vue/releases"><img src="https://badgen.net/github/release/Matgenix/datalab-item-plugin-example-custom-vue?icon=github&color=blue"></a>
<a href="https://github.com/Matgenix/datalab-item-plugin-example-custom-vue"><img src="https://badgen.net/github/license/Matgenix/datalab-item-plugin-example-custom-vue?icon=license&color=purple"></a>
<a href="https://Matgenix.github.io/datalab-item-plugin-example-custom-vue"><img src="https://github.com/Matgenix/datalab-item-plugin-example-custom-vue/actions/workflows/docs.yml/badge.svg"></a>
</div>

datalab-item-plugin-example-custom-vue is a [*datalab*](https://datalab-org.io) plugin generated using the [datalab-item-plugin-template](https://github.com/Matgenix/datalab-item-plugin-template) template.

> [!NOTE]
> This is an **example plugin**, kept as a reference for custom item type authors — it is
> not meant to be deployed as-is. It shows an item type rendered by its own custom Vue
> panel. Its companion example,
> [datalab-item-plugin-example](https://github.com/Matgenix/datalab-item-plugin-example),
> shows the simpler kind (fields rendered automatically from schema annotations, no
> JavaScript) and provides the `solutions` item type this plugin's items are blended from —
> install both together.

It registers the custom item type `mixed_solutions` — a solution blended by volume from
`solutions` items (implemented by
[`datalab_item_plugin_example_custom_vue.models.MixedSolution`](src/datalab_item_plugin_example_custom_vue/models.py)) — with *datalab*
via the `pydatalab.item_types` entry point, making it available through the standard item
endpoints and the web UI.

The item's fields are rendered in the web UI by the custom panel
[`MixedSolutionPanel.vue`](src/datalab_item_plugin_example_custom_vue/webapp/MixedSolutionPanel.vue),
which is discovered and bundled into the webapp by running `uv run invoke dev.collect-plugin-panels`
in the *datalab* repository after installing this plugin (see [INSTALL.md](INSTALL.md)).

Releases are created via semantic version tags on [GitHub](https://github.com/Matgenix/datalab-item-plugin-example-custom-vue/releases).
