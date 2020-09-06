# from django.urls import path, include
# from django.contrib import admin

from django.contrib import admin
from django.urls import path, include

app_name = 'home'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]


# urlpatterns = [
#     path('', include(('home.urls', 'home'), namespace='home')),
#     path('admin/', admin.site.urls),
#     path('index/', include('home.urls')),
# ]
