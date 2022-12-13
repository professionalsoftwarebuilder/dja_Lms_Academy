from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static, settings


urlpatterns = [
    # Examples:
    # path(r'^$', 'academicstoday_project.views.home', name='home'),
    # path(r'^blog/', include('blog.urls')),

    # #$# let op
    #path('admin/', include(admin.site.urls)),
    path('admin/', admin.site.urls),
               
    # This regex makes the default URL for the website to launch this view.
    path('', include('landpage.urls')),
    path('', include('registration.urls')),
    path('', include('login.urls')),
    path('', include('account.urls')),
    path('', include('registrar.urls')),
    path('', include('student.urls')),
    path('', include('teacher.urls')),
    path('', include('publisher.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [path('ckeditor/', include('ckeditor_uploader.urls'))]
