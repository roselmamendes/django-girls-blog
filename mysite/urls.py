from django.conf.urls import include, url
from django.contrib import admin
# Examples:
# url(r'^$', 'mysite.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
urlpatterns = [
    url(r'^admin/', include(admin.site.urls))
]
