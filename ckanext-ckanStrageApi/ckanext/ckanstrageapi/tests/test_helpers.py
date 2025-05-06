"""Tests for helpers.py."""

import ckanext.ckanstrageapi.helpers as helpers


def test_ckanstrageapi_hello():
    assert helpers.ckanstrageapi_hello() == "Hello, ckanstrageapi!"
