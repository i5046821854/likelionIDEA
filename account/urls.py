from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('register/', register_view, name = "signup"),
    path("select/", select, name="select"),
    path("edit/", edit_profile, name="edit_profile"),
    path("test/", test, name="test"),
] 