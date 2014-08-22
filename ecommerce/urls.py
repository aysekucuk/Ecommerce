from django.conf.urls import patterns, include, url
from users import urls as users_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ecommerce.views.home', name='home'),
    url(r'^login$', 'ecommerce.views.login', name='login'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^kullanici/', include(users_urls)),

)
