"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.ckanstrageapi.logic import validators


def test_ckanstrageapi_reauired_with_valid_value():
    assert validators.ckanstrageapi_required("value") == "value"


def test_ckanstrageapi_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.ckanstrageapi_required(None)
