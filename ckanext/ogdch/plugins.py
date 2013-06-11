import ckan
import ckan.plugins as p
import random
from pylons import config

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
        return {'get_css_version': self.get_css_version }

    def get_css_version(self):
        if config['ckanext.ogdch.css_version'] == 'rand':
            return random.randint(100000, 9999999999)

        return config['ckanext.ogdch.css_version']
