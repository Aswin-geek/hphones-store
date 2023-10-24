from django.contrib import admin
from hps.models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(PrdVariation)
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(OrderItem)
admin.site.register(Order)