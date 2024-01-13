from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Inventory)
admin.site.register(MenueItem)
admin.site.register(Recipe_list)
admin.site.register(Sales)
admin.site.register(SalesLines)

