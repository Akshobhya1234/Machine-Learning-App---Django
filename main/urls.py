from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    url(r'^$',views.search,name="search1"),

    path("search",views.search,name="search"),
    path("searchview",views.searchview,name="searchview"),
    path("selectChoice",views.selectChoice,name="selectChoice"),
    path("modelResultView",views.modelsResultview,name="modelResultView"),
    path("modelResultForm",views.modelResultSee,name="modelResultForm"),
]

