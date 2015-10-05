from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

# import pacs.urls
from pacs import views
import home.views

admin.autodiscover()

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'pacs', views.RawCommitteeTransactionsViewSet)


urlpatterns = [
    # Examples:
    # url(r'^', home.views.index, name='home'),
    # url(r'^decoder/', include(decoder.urls)),
    # url(r'^pacs/', include(pacs.urls)),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
]


# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'hackor.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^', include(pacs.urls)),
#     # url(r'^$', pacs.views.RawCommitteeTransactionsViewSet.as_view({'get':'list'})),
# )
