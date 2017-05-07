from __future__ import unicode_literals, print_function, division, absolute_import

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.views import defaults as default_views
from django.views.generic import TemplateView

# URLs with with i18n
urlpatterns = i18n_patterns(
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^reg/', TemplateView.as_view(template_name='pages/registry.html'), name="reg"),
    url(r'^programa/', include('pydaygal.schedule.urls', namespace="programa")),
    url(r'^code-of-conduct/$', TemplateView.as_view(
        template_name='pages/code_of_conduct.html'), name="code-of-conduct"),
    url(r'^info/$', TemplateView.as_view(template_name='pages/info.html'), name="info"),
    url(r'^cfp/', TemplateView.as_view(template_name='pages/cfp.html'), name="cfp"),
    url(r'^speakers/', include('pydaygal.speakers.urls', namespace="speakers")),
    url(r'^users/', include('pydaygal.users.urls', namespace="users")),
    url(r'^workshops/', include('pydaygal.workshops.urls', namespace="workshops")),
    url(r'^multimedia/', include('pydaygal.multimedia.urls', namespace="multimedia")),
)

# URLs without i18n
urlpatterns += [
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

# Override all links if the landing page is set
if settings.LANDING_GLOBAL_REDIRECT:
    urlpatterns = [
        url(r'^$', TemplateView.as_view(
            template_name='pages/landing.html'), name="landing"),
    ]

# Django Admin, use {% url 'admin:index' %}
admin.site.site_header = _('%s Admin') % settings.CONFERENCE_TITLE
urlpatterns += [
    url(settings.ADMIN_URL, admin.site.urls),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]

    # If is installed debug_toolbar, add its urls
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]

    # Only access directly to MEDIA when DEBUG is True
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
