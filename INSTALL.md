# Installation

> [!IMPORTANT]
> Custom item types are not yet part of a released *datalab* version. Until they
> are, this plugin must be installed against the `ml-evs/custom-items` feature
> branch of [datalab-org/datalab](https://github.com/datalab-org/datalab) (the
> development environment below already does this via `[tool.uv.sources]` in
> `pyproject.toml`).

## Development installation

We recommend you use [`uv`](https://astral.sh/uv) for managing virtual environments and Python versions.

Once you have `uv` installed, you can clone this repository and install the package in a fresh virtual environment with:

```
git clone git@github.com:Matgenix/datalab-item-plugin-example-custom-vue
cd datalab-item-plugin-example-custom-vue
uv sync --all-extras --dev
```

You can activate `pre-commit` in your local repository with `uv run pre-commit install`.
This will call `pre-commit` automatically on every commit to check for code style and other issues, and will also be used in the CI.

## Installation and deployment as a *datalab* plugin

It is also possible install this plugin on a local *datalab* instance (for e.g., testing).

The simplest way to do this is to activate the virtual environment in which
*datalab* is installed, then run `uv pip install .` in the root of
this repository which will install the package in the current Python
environment. This will be clobbered by any `uv sync` command, so it is not
recommended for development.

The alternative is to make a branch of your local *datalab* and add the plugin
to your local *datalab* `pydatalab/pyproject.toml` as an extra.
You also need to provide the source of the plugin in the `[tool.uv.sources]`
section of the `pyproject.toml` file, which could point to a public GitHub
repository or a local path. For example:

```toml
[project.optional-dependencies]
plugins = [
    "my-local-plugin",
    "my-git-plugin",
]

[tool.uv.sources]
my-local-plugin = { path = "../path/to/my-local-plugin" }
my-git-plugin = { git = "https://github.com/user/plugin-repo.git" }
```

Running `uv lock` will then create a lockfile with the plugin included, and you
can then run `uv sync` to install the plugin in your local *datalab* instance.

### Bundling the custom web UI panel

This plugin ships a custom Vue panel
(`src/datalab_item_plugin_example_custom_vue/webapp/MixedSolutionPanel.vue`). The *datalab*
webapp does not load plugin JavaScript at runtime; instead, after installing
this plugin into the *datalab* API environment, run (from the `pydatalab/`
directory of the *datalab* repository):

```
uv run invoke dev.collect-plugin-panels
```

This discovers `webapp/<ClassName>Panel.vue` components from all installed
`pydatalab.item_types` plugins, copies them into `webapp/src/plugins/` and
regenerates the panel registry. Run it after every plugin install or update,
and before building the webapp.

### Deploying plugins in production

The process of deploying plugins in production is similar to the local approach
above (for now) and depends on how you manage your *datalab* deployment.  The recommended approach is to use the
[`datalab-ansible-terraform`](https://github.com/datalab-industries/datalab-ansible-terraform)
repository to manage your *datalab* deployment, which uses Ansible
to deploy *datalab* on a remote server. In this case, you can create a branch of the
repository for your deployment and add the plugin as an extra in the
`pyproject.toml` file of the `pydatalab` component, as described above. You can
then run `uv lock` and `uv sync` to install the plugin in your production
environment.
