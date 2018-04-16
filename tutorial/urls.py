from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include('snippets.urls')),
]
