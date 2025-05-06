"""Tests for auth.py."""

import pytest

import ckan.tests.factories as factories
import ckan.tests.helpers as test_helpers
import ckan.model as model


@pytest.mark.ckan_config("ckan.plugins", "ckanstrageapi")
@pytest.mark.usefixtures("with_plugins", "clean_db")
def test_ckanstrageapi_get_sum():
    user = factories.User()
    context = {
        "user": user["name"],
        "model": model
    }
    assert test_helpers.call_auth(
        "ckanstrageapi_get_sum", context=context)
