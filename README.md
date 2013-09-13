ckanext-ogdch
=============

CKAN templates and translations for opendata.admin.ch

## Installation

Use `pip` to install this plugin. This example installs it in `/home/www-data`

```bash
source /home/www-data/pyenv/bin/activate
pip install -e git+https://github.com/ogdch/ckanext-ogdch.git#egg=ckanext-ogdch --src /home/www-data
cd /home/www-data/ckanext-ogdch
python setup.py develop
```

Make sure to add *`ogdch`* to `ckan.plugins` in your config file.
