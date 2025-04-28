# This Repo is used for demo submodule repo

Folder structure
```
mypackage
│   .gitignore
│   .gitmodules
│   pyproject.toml
│   README.md
│   __version__.py
│
└───src
    │   __init__.py
    │
    └───components
        │   __init__.py
        │
        ├───component-a (submodule)
        │       component.py
        │       README.md
        │
        └───component-b (submodule)
                component.py
                README.md

```

Study on gitsubmodule: https://git-scm.com/book/en/v2/Git-Tools-Submodules

How to clone for Repo with submodules
```shell
git clone --recurse-submodules https://github.com/linnkern/mypackage.git
```

How to pull for Repo with submodules
```shell
git pull --recurse-submodules
```

How to update submodules
```shell
git submodule update --remote
```