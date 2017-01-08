from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from juanwolf_fr import views

admin.autodiscover()

urlpatterns = [
    # Internationalization
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # Resume
    url(r'^resume/', include('resume.urls')),
    url(r'^about/$', views.AboutView.as_view(), name="about"),
    # Index
    url(r'^$', views.IndexView.as_view(), name="index")
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
