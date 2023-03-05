from django.contrib import admin
from django.urls import path
from test_api_app.views import Simple, SimpleGenerics, SimpleGenericsUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', Simple.as_view()),
    path('api/<int:id>', Simple.as_view()),
    path('api-generics/', SimpleGenerics.as_view()),
    path('api-generics/<int:id>', SimpleGenericsUpdate.as_view())
]
