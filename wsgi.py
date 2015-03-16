import os
import dotenv

dotenv.read_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.prod")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

application = Cling(MediaCling(get_wsgi_application()))
