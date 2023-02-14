import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_portfolio.settings")

django.setup()

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
