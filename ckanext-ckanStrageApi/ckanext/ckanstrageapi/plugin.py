import logging

import ckan.plugins as plugins
import ckanext.ckanstrageapi.logic.auth as auth
import ckantoolkit as toolkit

log = logging.getLogger(__name__)

import ckanext.ckanstrageapi.cli as cli
import ckanext.ckanstrageapi.logic.action as action


class CkanstrageapiPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.IClick)

    def get_actions(self):
        return action.get_actions()

    def get_commands(self):
        return cli.get_commands()
    
    def get_auth_functions(self):
        return auth.get_auth_functions()
