from django.conf.urls import include, url
from django.contrib import admin

import pacs.urls


urlpatterns = [
    # Examples:
    url(r'^', 'home.views.index', name='home'),
    # url(r'^decoder/', include(decoder.urls)),
    url(r'^pacs/', include(pacs.urls)),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
