![Python checks](https://github.com/leakquicked/hashvault/actions/workflows/python-checks.yml/badge.svg)

# HashVault

Build a local SHA-256 manifest.

## Requirements
Python 3.10+, standard library only.

## Usage
`python hashvault.py --help`

Processes local files only; no network requests or uploads. Do not publish confidential inventories.

## Tests
`python -m unittest discover -s tests -v`
