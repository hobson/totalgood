from django.conf.urls import include, url
from django.contrib import admin

import conceive.urls


urlpatterns = [
    # Examples:
    url(r'^', 'home.views.index', name='home'),
    # url(r'^decoder/', include(decoder.urls)),
    url(r'^conceive/', include(conceive.urls)),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
