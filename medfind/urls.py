from django.contrib import admin
from django.urls import path

from .views import home

from users.views import (
    register,
    user_login,
    user_logout,
    search_medicine,
    nearby_stores,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("login/", user_login, name="login"),

    path("register/", register, name="register"),

    path("logout/", user_logout, name="logout"),

    path("search/", search_medicine, name="search"),

    path("nearby-stores/", nearby_stores, name="nearby_stores"),
]
