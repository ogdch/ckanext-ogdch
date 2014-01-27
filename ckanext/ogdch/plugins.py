import ckan.plugins as p
from ckan.lib.base import c
from ckan import model
from ckan.logic import NotFound, get_action
import random
from pylons import config

import logging
log = logging.getLogger(__name__)


class OgdchTheme(p.SingletonPlugin):
    """
    Plugin containg the theme for OGDCH
    """
    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)

    def update_config(self, config):
        # add our templates
        p.toolkit.add_template_directory(config, 'templates/ckan')

    def get_helpers(self):
        return {
            'get_css_version': self.get_css_version,
            'get_license_url': self.get_license_url,
            'get_organization_url': self.get_organization_url,
        }

    def get_css_version(self):
        if config['ckanext.ogdch.css_version'] == 'random':
            return random.randint(100000, 9999999999)

        return config['ckanext.ogdch.css_version']

    def get_license_url(self, pkg_dict):
        for extra in pkg_dict.get('extras', []):
            if extra.get('key') == 'license_url':
                return extra.get('value')
        return ''

    def get_organization_url(self, organization_id):
        context = {
            'model': model,
            'user': c.user
        }
        try:
            org = get_action('organization_show')(
                context,
                {
                    'id': organization_id
                }
            )
            for extra in org.get('extras', []):
                if extra.get('key') == 'website':
                    return extra.get('value').rstrip('/')
            return ''
        except NotFound:
            log.error('Organization %s not found' % organization_id)
            return ''
