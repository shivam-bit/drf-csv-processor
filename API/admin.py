from django.contrib import admin
from .models import csv_product,customer,file_uploads
# Register your models here.
admin.site.register(customer)
admin.site.register(csv_product)
admin.site.register(file_uploads)