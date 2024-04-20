from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tailoring/', include('tailoring.urls')),  # Include your app’s URLs
]
