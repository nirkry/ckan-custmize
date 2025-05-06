from flask import Blueprint


ckanstrageapi = Blueprint(
    "ckanstrageapi", __name__)


def page():
    return "Hello, ckanstrageapi!"


ckanstrageapi.add_url_rule(
    "/ckanstrageapi/page", view_func=page)


def get_blueprints():
    return [ckanstrageapi]
