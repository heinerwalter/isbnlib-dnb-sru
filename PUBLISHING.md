# Publishing to PyPI

This document describes how to upload a Python package to the Python Package Index (PyPI).

## Prerequisites

- A PyPI account (register at [pypi.org](https://pypi.org/account/register/))
- An API token with "Entire account" scope (create at [pypi.org/manage/account/#api-tokens](https://pypi.org/manage/account/#api-tokens))
- `build` and `twine` installed:
  ```bash
  python3 -m pip install --upgrade build twine
  ```


## Steps

1. **Generate distribution archives**
   ```bash
   python3 -m build
   ```
   This creates a `dist/` directory with `.whl` and `.tar.gz` files.

2. **Upload to PyPI**
   ```bash
   python3 -m twine upload dist/*
   ```
   When prompted, paste your API token (including the `pypi-` prefix).


## Testing with TestPyPI

To test before publishing to the real PyPI:

1. Register at [test.pypi.org](https://test.pypi.org/account/register/)
2. Create an API token for TestPyPI
3. Upload to TestPyPI:
   ```bash
   python3 -m twine upload --repository testpypi dist/*
   ```
4. Install and test from TestPyPI:
   ```bash
   python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps your-package-name
   ```


## Notes

- Always upload both the wheel (`.whl`) and source (`.tar.gz`) distributions.
- The `--no-deps` flag prevents installing dependencies from TestPyPI, which may fail.
- Once uploaded to PyPI, packages cannot be deleted; use TestPyPI for testing.
