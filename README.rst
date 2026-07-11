
.. image:: https://github.com/heinerwalter/isbnlib-dnb-sru/workflows/tests/badge.svg
    :target: https://github.com/heinerwalter/isbnlib-dnb-sru/actions
    :alt: Built Status

.. image:: https://img.shields.io/github/issues/heinerwalter/isbnlib-dnb-sru/bug.svg?label=bugs&style=flat
    :target: https://github.com/heinerwalter/isbnlib-dnb-sru/labels/bug
    :alt: Bugs

.. image:: https://img.shields.io/pypi/dm/isbnlib-dnb-sru.svg?style=flat
    :target: https://pypi.org/project/isbnlib-dnb-sru/
    :alt: PYPI Downloads



A metadata plugin for ``isbnlib`` (https://pypi.python.org/pypi/isbnlib) using the SRU service
of the Deutsche Nationalbibliothek (DNB; German national library) ``services.dnb.de/sru/dnb`` (for books in German).
See documentation at: https://www.dnb.de/DE/Professionell/Metadatendienste/Datenbezug/SRU/sru_node.html

To install, from the command line, enter (in some cases you have to precede the command with ``sudo``):

.. code-block:: bash

    $ pip install isbnlib-dnb-sru


After install, a new metadata provider (``dnb-sru``) is available in isbnlib.

For available plugins check_ here.



.. _check: https://pypi.python.org/pypi?%3Aaction=search&term=isbnlib_&submit=search
