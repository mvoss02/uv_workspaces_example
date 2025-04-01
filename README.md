# uv Workspace Example

This repository serves as an example of how **uv workspaces** function. The official documentation can be found here: [uv Workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/).

## **What is a uv Workspace?**

In `uv`, a **workspace** allows you to manage multiple Python projects (packages) under a single root directory while treating them as a cohesive unit. This is particularly useful for **monorepos** or scenarios where you are developing multiple interdependent packages together (e.g., libraries, microservices, or related modules).

This repository provides a simple but fully working example demonstrating the use of `uv` workspaces.

---

## **Project Initialization**

To get started, navigate to the directory where you want to store your project and create a new directory:

```bash
mkdir NAME_OF_NEW_PROJECT && cd NAME_OF_NEW_PROJECT
```

Then, initialize the project using `uv`:

```bash
uv init
```

This command creates a `pyproject.toml` file and sets up the basic project structure.

---

## **pyproject.toml**

The `pyproject.toml` file is a standardized configuration file for Python projects. It defines **metadata**, **dependencies**, and **build settings**, replacing `requirements.txt`. `uv` leverages `pyproject.toml` for:

- Fast dependency resolution
- Lockfile management (`uv.lock`)
- Workspace support (managing multiple related packages in a single repository)

Example `pyproject.toml` structure for a workspace:

```toml
[project]
name = "uv-workspaces-example"
version = "0.1.0"
description = "Root project"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "data-ingest",
    "data-pre",
    "my-package-1",
    "my-package-2",
    "numpy>=2.2.4",
]

[tool.uv.sources]
my-package-1 = { workspace = true }
my-package-2 = { workspace = true }
data-ingest = { workspace = true }
data-pre = { workspace = true }

[tool.uv.workspace]
members = [
    "packages/my_package_1",
    "packages/my_package_2",
    "services/data_ingestion",
    "services/data_preprocessing"
]
```

This configuration defines multiple workspace members that `uv` will manage together.

---

## **uv Functionality**

### **Creating a Virtual Environment**

```bash
uv venv
```

### **Installing Dependencies**

Sync packages specified in `pyproject.toml`:

```bash
uv sync                          # Install dependencies for the current workspace
uv sync --package PACKAGE_NAME   # Install dependencies for a specific package
uv sync --all-packages           # Install dependencies for all workspace members
```

### **Initializing a Directory**

```bash
uv init NAME_OF_DIRECTORY       # Initializes a regular directory
uv init NAME_OF_DIRECTORY --lib # Initializes a package (adds it to the workspace)
```

Using the `--lib` flag automatically registers the package in `pyproject.toml` under `[tool.uv.workspace]`.

### **Building a Package**

```bash
uv build                        # Builds the current package using the specified build system
uv build --package PACKAGE_NAME # Builds a specific package into a `.whl` file
```

### **Adding External Dependencies**

```bash
uv add PACKAGE_NAME             # Adds a package (equivalent to pip install PACKAGE_NAME)
uv add "PACKAGE_NAME>=0.20"     # Adds a package with a version constraint
uv pip install PACKAGE_NAME     # Installs package via pip
```

Note: Libraries defined via `uv init NAME_OF_DIRECTORY --lib` can be imported directly.

### **Removing Dependencies**

```bash
uv remove PACKAGE_NAME
```

---

## **Conclusion**

`uv` workspaces simplify managing multiple Python projects by offering fast dependency resolution, efficient builds, and seamless package management. This repository provides a foundation for understanding and working with `uv` in a real-world setup.

For more details, visit the [official uv documentation](https://docs.astral.sh/uv/concepts/projects/workspaces/).
