from django.urls import path
from .views import *

urlpatterns = [
path("", home, name="home"),
path("about", about, name="about"),
path("inventory", InventoryListView.as_view(), name="inv_list"),
path("inventory_add", CreateIventoryView.as_view(), name="inv_add"),
path("inventory/<pk>/update", UpdateIventoryView.as_view(), name="inv_update"),
path("menu", MenuListView.as_view(), name="menu_list"),
path("menu/<pk>/update", UpdateMenuView.as_view(), name="menu_update"),
path("menu_add", CreateMenueView.as_view(), name="menu_add"),
path("recipe/<menu_pk>", menu_recipe, name="recipe_add"),
path("sale", sale_view, name='sale_add'),
path("sale_add_item", sale_add_item, name="sale_add_item"),
path("sale_del_item/<pk>", sale_remove_item, name= 'sale_remove_item'),
path("sale_complete/<pk>", complete_sale, name="complete_sale"),
path("sale_cancel/<pk>", cancel_sale, name="cancel_sale")
]