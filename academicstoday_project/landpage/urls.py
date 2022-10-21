#from django.conf.urls import patterns, include, url
from django.urls import *

from landpage.views import txt
from landpage.views import landpage
from landpage.views import privacy
from landpage.views import terms
from landpage.views import forgot_password
from landpage.views import google

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # Custom Files
    path('robots\.txt', txt.robots_txt_page, name='robots'),
    path('humans\.txt', txt.humans_txt_page, name='humans'),
                       
    # Google Verify
    path('googlee81f1c16590924d1.html', google.google_verify_page, name='google_plus_verify'),
    path('googlee81f1c16590924d1', google.google_verify_page),
                       
    # Landpage
    path('', landpage.landpage_page, name='landpage'),
    path('landpage', landpage.landpage_page),
    path('course_preview_modal', landpage.course_preview_modal),
    path('save_contact_us_message', landpage.save_contact_us_message),
                       
    # Off-Convas Stuff
    path('terms', terms.terms_page, name='terms'),
    path('privacy', privacy.privacy_page, name='privacy'),
    path('forgot_password', forgot_password.forgot_password_page, name='forgot_password'),
    path('reset_password', forgot_password.reset_password, name='reset_password'),
                       
    # Sitemap
    path('sitemap\.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

# Captchas
# urlpatterns += [
#     path('captcha/', include('captcha.urls')),
# ]