from django.contrib import admin
from django.urls import path
from articles import views
from articles.views import archive

urlpatterns = [
    path('admin/', admin.site.urls),
    path('archive/', archive, name='archive'),
]
