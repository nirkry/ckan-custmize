import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def ckanstrageapi_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "ckanstrageapi_get_sum": ckanstrageapi_get_sum,
    }
