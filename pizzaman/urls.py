from django.urls import path
from .views import *

urlpatterns = [
path("", home, name="home"),
path("about", about, name="about"),
path("inventory", InventoryListView.as_view(), name="inv_list"),
path("inventory_add", CreateIventoryView.as_view(), name="inv_add"),
path("inventory/<pk>/update", UpdateIventoryView.as_view(), name="inv_update"),

]