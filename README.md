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
> JavaScript) and provides the `example:solutions` item type this plugin's items are blended
> from — install both together.

It registers the canonical custom item type `example:mixed-solutions` — a solution blended by
volume from `example:solutions` items (implemented by
[`datalab_item_plugin_example_custom_vue.models.MixedSolution`](https://github.com/Matgenix/datalab-item-plugin-example-custom-vue/blob/main/src/datalab_item_plugin_example_custom_vue/models.py)) — with *datalab*
via the `pydatalab.item_types` entry point, making it available through the standard item
endpoints and the web UI.

The entry-point key is only a packaging-safe discovery name. The model's `type` literal is the
canonical identifier used by *datalab*.

The complete canonical identifier is used wherever the type is referenced. Its namespace and type
name are conceptual components only; *datalab* does not store or query them separately at present.

The item's fields are rendered in the web UI by the custom panel
[`MixedSolutionPanel.vue`](https://github.com/Matgenix/datalab-item-plugin-example-custom-vue/blob/main/src/datalab_item_plugin_example_custom_vue/webapp/MixedSolutionPanel.vue),
which is discovered and bundled automatically when *datalab* installs its declared plugins and
builds the webapp (see [INSTALL.md](INSTALL.md)).

Releases are created via semantic version tags on [GitHub](https://github.com/Matgenix/datalab-item-plugin-example-custom-vue/releases).
