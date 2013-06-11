import ckan
import ckan.plugins as p

class OgdchTheme(p.SingletonPlugin):
    p.implements(p.IConfigurer)

    def update_config(self, config):
        # add our templates
        p.toolkit.add_template_directory(config, 'templates/ckan')
