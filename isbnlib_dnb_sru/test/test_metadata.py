# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""tests for metadata."""

import json
from isbnlib import meta
from .._dnb_sru import query


def _is_metadata_filled(book,
                        has_publisher=True,
                        has_year=True,
                        has_language=True,
                        has_place=True,
                        has_pages=True,
                        has_edition=True):
    """Check if the metadata of a book is filled."""
    result = True
    if not book.get('ISBN-13') and not book.get('ISBN-10'):
        print("ISBN is missing")
        result = False
    if not book.get('Title'):
        print("Title is missing")
        result = False
    if not book.get('Authors'):
        print("Authors are missing")
        result = False
    if has_publisher and not book.get('Publisher'):
        print("Publisher is missing")
        result = False
    if has_year and not book.get('Year'):
        print("Year is missing")
        result = False
    if has_language and not book.get('Language'):
        print("Language is missing")
        result = False
    if has_place and not book.get('Place'):
        print("Place is missing")
        result = False
    if has_pages and not book.get('Pages'):
        print("Pages is missing")
        result = False
    if has_edition and not book.get('Edition'):
        print("Edition is missing")
        result = False

    if not result:
        print(json.dumps(book, indent=2))
    return result


def test_query():
    """Test services.dnb.de/sru/dnb."""
    bookA = query('9783608126051')
    bookB = query('9783608987492')
    bookC = query('9783608938296')
    assert (len(repr(bookA)) > 100) == True
    assert (len(repr(bookB)) > 100) == True
    assert (len(repr(bookC)) > 100) == True

    assert _is_metadata_filled(bookA, has_pages=False, has_edition=False)
    assert _is_metadata_filled(bookB)
    assert _is_metadata_filled(bookC)

def test_query_missing():
    """Test services.dnb.de/sru/dnb (missing data)."""
    assert (len(repr(query('9781849692341'))) <= 2) == True
    assert (len(repr(query('9781849692343'))) <= 2) == True


def test_query_wrong():
    """Test services.dnb.de/sru/dnb (wrong data)."""
    assert (len(repr(query('9780000000'))) <= 2) == True
