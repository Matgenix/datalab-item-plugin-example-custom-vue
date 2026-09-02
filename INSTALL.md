# Installation

## Development installation

Clone the plugin and install its development environment with [`uv`](https://astral.sh/uv):

```shell
git clone git@github.com:Matgenix/datalab-item-plugin-example-custom-vue
cd datalab-item-plugin-example-custom-vue
uv sync --all-extras --dev
```

## Installation in *datalab*

Add both example plugins to `plugins.toml` at the root of the *datalab* checkout:

```toml
dependencies = [
    "datalab-item-plugin-example",
    "datalab-item-plugin-example-custom-vue",
]

[tool.uv.sources]
datalab-item-plugin-example = { git = "https://github.com/Matgenix/datalab-item-plugin-example.git" }
datalab-item-plugin-example-custom-vue = { git = "https://github.com/Matgenix/datalab-item-plugin-example-custom-vue.git" }
```

For local development, use editable paths instead of the Git sources:

```toml
[tool.uv.sources]
datalab-item-plugin-example = { path = "../datalab-item-plugin-example", editable = true }
datalab-item-plugin-example-custom-vue = { path = "../datalab-item-plugin-example-custom-vue", editable = true }
```

Install *datalab* and its declared plugins from the `pydatalab/` directory:

```shell
uv run invoke dev.install
```

The custom Vue panel is collected automatically during installation and builds.
