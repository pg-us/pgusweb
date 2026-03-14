from django.urls import re_path
from django.views.generic import RedirectView

PRELOAD_URLS = [
    re_path(r'^diversity/$', RedirectView.as_view(url='/community_development/', permanent=True)),
]
