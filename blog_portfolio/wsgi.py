"""
WSGI config for blog_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_portfolio.settings')

# PRODUCTION

app = WhiteNoise(
    get_wsgi_application(),
    root="./staticfiles_build/static"
)
app.add_files("./staticfiles_build/static", prefix="more-files/")

# DEVELOPMENT

# application = get_wsgi_application()
