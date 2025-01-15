from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/' , include('send_emails.urls') ),
    path('account/' , include('accounts.urls'))
]
