from django.contrib import admin
from django.urls import path
from test_api_app.views import Simple

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Simple.as_view())
]
