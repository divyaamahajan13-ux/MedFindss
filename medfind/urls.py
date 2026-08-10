from django.contrib import admin
from django.urls import path
from .views import home
from users.views import register, search_medicine, nearby_stores

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("search/", search_medicine, name="search"),
    path("admin/", admin.site.urls),
    path("nearby-stores/", nearby_stores, name="nearby_stores"),
]
