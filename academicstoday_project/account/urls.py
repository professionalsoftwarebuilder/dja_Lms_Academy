from django.urls import include, path
from account.views import mail
from account.views import profile
from account.views import setting
from account.views import donate

urlpatterns = [
    path('profile', profile.profile_page),
    path('update_user', profile.update_user),
    path('inbox', mail.mail_page),
    path('send_private_message', mail.send_private_message),
    path('view_private_message', mail.view_private_message),
    path('delete_private_message', mail.delete_private_message),
    path('settings', setting.settings_page),
    path('update_password', setting.update_password),
    path('donate', donate.donate_page),
]