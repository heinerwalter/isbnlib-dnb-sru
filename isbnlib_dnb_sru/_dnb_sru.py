# -*- coding: utf-8 -*-
"""Query the services.dnb.de/sru/dnb service for metadata."""

import logging
from xml.dom.minidom import parseString

from isbnlib.dev import stdmeta
from isbnlib.dev.webquery import query as webquery

LOGGER = logging.getLogger(__name__)
UA = 'isbnlib (gzip)'
SERVICE_URL = 'https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query={isbn}'


def _get_text(topnode):
    """Get the text values in the child nodes."""
    text = ""
    for node in topnode.childNodes:
        if node.nodeType == node.TEXT_NODE:  # pragma: no cover
            text = text + node.data
    return text

def _get_attributes_text(topnode):
    """Get the text values in the child nodes."""
    text = ""
    if not len(topnode.attributes) or 'rdf:resource' not in topnode.attributes._attrs:  # pragma: no cover
        return text
    node = topnode.attributes._attrs['rdf:resource']
    text = node.value
    return text


def parser_sru(xml):
    """Parse the response from the SRU service."""
    # handle special case
    if '<error>' in xml:  # pragma: no cover
        return {}
    # parse xml and extract canonical fields
    dom = parseString(xml)
    # metadata fields found in the XML response of services.dnb.de/sru/dnb
    # - first tuple element: Result field name
    # - second tuple element: XML tag name
    # - third tuple element: where the content is stored: tag 'content' or 'attributes'
    fields = [
        ('ISBN-13', 'bibo:isbn13', 'content'),
        ('ISBN-10', 'bibo:isbn10', 'content'),
        ('Title', 'dc:title', 'content'),
        ('Authors', 'rdau:P60327', 'content'),
        ('Publisher', 'dc:publisher', 'content'),
        ('Year', 'dcterms:issued', 'content'),
        ('Place', 'rdau:P60163', 'content'),
        ('Language', 'dcterms:language', 'attributes'),
        ('Pages', 'isbd:P1053', 'content'),
        ('Edition', 'rdau:P60521', 'content'),
    ]
    metadata = {}
    try:
        # get all records from the XML response
        records = dom.getElementsByTagName("record")
        if not len(records):
            return None

        for key, field, type in fields:
            nodes = records[0].getElementsByTagName(field)
            if type == 'attributes':
                txt = '|'.join([_get_attributes_text(node) for node in nodes])
            else:
                txt = '|'.join([_get_text(node) for node in nodes])
            metadata[key] = txt
        # cleaning
        metadata['Publisher'] = metadata['Publisher'].split('|')[0] \
            if metadata['Publisher'] else ''
        authors = metadata['Authors'].split('|') if metadata['Authors'] else []
        metadata['Authors'] = [author.strip('0123456789,- ') for author in authors]
        metadata['Year'] = ''.join(c for c in metadata['Year'] if c.isdigit())[:4]\
            if metadata['Year'] else ''
        metadata['Title'] = metadata['Title'].replace(' :', ':').replace('<', '').replace('>', '') \
            if metadata['Title'] else ''
        metadata['Language'] = metadata['Language'].split('/')[-1].strip(' ') \
            if metadata['Language'] and '/' in metadata['Language'] else ''
        if metadata['Language'] == 'ger':
            metadata['Language'] = 'de'
        metadata['Pages'] = metadata['Pages'].lower() \
            .replace('s.', '').replace('seiten', '').replace('p.', '').replace('pages', '').strip(' .,-') \
            if metadata['Pages'] else ''
        metadata['Edition'] = metadata['Edition'].split(':')[0].strip(' ') \
            if metadata['Edition'] and ':' in metadata['Edition'] else ''

        metadata['ImageURL'] =(
            'https://portal.dnb.de/opac/mvb/cover?isbn=' + metadata['ISBN-13']) if metadata['ISBN-13'] \
            else ('https://portal.dnb.de/opac/mvb/cover?isbn=' + metadata['ISBN-10'] if metadata['ISBN-10'] else '')

        return metadata
    except Exception as exc:  # pragma: no cover
        LOGGER.debug('Check the parsing for services.dnb.de/sru/dnb (%r)', exc, exc_info=True)
        return metadata


def _mapper(isbn, records):
    """Make records canonical.

    canonical: ISBN-13, Title, Authors, Publisher, Year, Language
    """
    # handle special case
    if not records:  # pragma: no cover
        return {}
    # add ISBN-13
    records['ISBN-13'] = str(isbn)
    # call stdmeta for extra cleaning and validation
    return stdmeta(records)


def query(isbn):
    """Query the SRU service for metadata."""
    data = webquery(
        SERVICE_URL.format(isbn=isbn), user_agent=UA, parser=parser_sru)
    if not data:  # pragma: no cover
        LOGGER.debug('No data from services.dnb.de/sru/dnb for isbn %s', isbn)
        return {}
    return _mapper(isbn, data)


# for debugging:
#if __name__ == '__main__':
#    query('9783608126051')
