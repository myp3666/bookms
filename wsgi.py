import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append('/opt/www')

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
