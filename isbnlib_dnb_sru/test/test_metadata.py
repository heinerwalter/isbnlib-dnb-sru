# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""tests for metadata."""

from isbnlib import meta
from .._dnb_sru import query


def test_query():
    """Test services.dnb.de/sru/dnb with 'low level' queries."""
    assert (len(repr(query('9783608126051'))) > 100) == True
    assert (len(repr(query('9783608987492'))) > 100) == True
    assert (len(repr(query('9783608938296'))) > 100) == True


def test_query_missing():
    """Test services.dnb.de/sru/dnb with 'low level' queries (missing data)."""
    assert (len(repr(query('9781849692341'))) <= 2) == True
    assert (len(repr(query('9781849692343'))) <= 2) == True


def test_query_wrong():
    """Test services.dnb.de/sru/dnb with 'low level' queries (wrong data)."""
    assert (len(repr(query('9780000000'))) <= 2) == True
