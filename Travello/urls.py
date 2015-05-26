from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'rail.views.home', name='home'),
    url(r'^train/$', 'rail.views.train', name='train'),
    url(r'^rdet/$','rail.views.rdet',name='rdet'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
