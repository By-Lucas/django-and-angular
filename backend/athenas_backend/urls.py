from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls', namespace='accounts')),
    path('people/', include('peoples.urls', namespace='people'))
]
