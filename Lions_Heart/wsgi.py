"""
WSGI config for Lions_Heart project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys


from django.core.wsgi import get_wsgi_application


sys.path.append('/lions_heart/lions_heart_env/Lions_Heart')

sys.path.append('/lions_heart/lions_heart_env/Lib/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Lions_Heart.settings")

application = get_wsgi_application()






