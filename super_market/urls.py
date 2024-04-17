from django.urls import path
from super_market.views import (
    index,
    return_item,
    search_item,
    sell,
    login_view,
    logout_view,
    add_page,
    bell,
    get_data_about_prodeuct,

)


urlpatterns = [
    path("", index, name="home"),
    path("search", search_item, name="search"),
    path("add", add_page, name="add"),
    path("sell", sell, name="sell"),
    path("return", return_item, name="return"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("bell", bell, name="bell"),
    path("data", get_data_about_prodeuct, name="get_data"),

]
