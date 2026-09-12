# isbnlib_dnb_sru

[![Built Status](https://github.com/heinerwalter/isbnlib-dnb-sru/workflows/tests/badge.svg)](https://github.com/heinerwalter/isbnlib-dnb-sru/actions)

[![Bugs](https://img.shields.io/github/issues/heinerwalter/isbnlib-dnb-sru/bug.svg?label=bugs&style=flat)](https://github.com/heinerwalter/isbnlib-dnb-sru/labels/bug)

[![PYPI Downloads](https://img.shields.io/pypi/dm/isbnlib-dnb-sru.svg?style=flat)](https://pypi.org/project/isbnlib-dnb-sru/)

A metadata plugin for `isbnlib` (https://pypi.python.org/pypi/isbnlib) using the SRU service
of the Deutsche Nationalbibliothek (DNB; German national library) `services.dnb.de/sru/dnb` (for books in German).
See documentation at: https://www.dnb.de/DE/Professionell/Metadatendienste/Datenbezug/SRU/sru_node.html


## Installation

To install, from the command line, enter (in some cases you have to precede the command with `sudo`):

```bash
$ pip install isbnlib-dnb-sru
```

After installation, a new metadata provider (`dnb-sru`) is available in isbnlib.

For other available isbnlib plugins check [here](https://pypi.python.org/pypi?%3Aaction=search&term=isbnlib_&submit=search).


## Development

For developing and contributing see [CONTRIBUTING.md](CONTRIBUTING.md).
