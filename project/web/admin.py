from django.contrib import admin
from .models import *

class DesignPost(admin.ModelAdmin):
    list_display = ["id_code","type","model","quantity","Price_Per_Unit","Price_Per_Unit_Imp","inventory"]

class DesignPost_export(admin.ModelAdmin):
    list_display = ["id_bill","sparepart","quantity","price","DateTime"]

class DesignPost_supplier(admin.ModelAdmin):
    list_display = ["name","number"]
    search_fields = ['name',]

class DesignPost_wait(admin.ModelAdmin):
    list_display = ["id_import","sparepart","supplier","quantity","price","DateTime"]

class DesignPost_import(admin.ModelAdmin):
    list_display = ["id_import","sparepart","quantity","price","DateTime"]

class DesignPost_exbill(admin.ModelAdmin):
    list_display = ["id_bill","part_all"]

class DesignPost_costumer(admin.ModelAdmin):
    list_display = ["license","name","number"]

class DesignPost_bill(admin.ModelAdmin):
    list_display = ["id_bill","customer_Car","total_Charge","DateTime"]

admin.site.register(sparepart,DesignPost)
admin.site.register(supplier,DesignPost_supplier)
admin.site.register(sparepart_order)
admin.site.register(import_wait,DesignPost_wait)
admin.site.register(import_part,DesignPost_import)
admin.site.register(export_part,DesignPost_export)
admin.site.register(export_bill,DesignPost_exbill)
admin.site.register(customer_car,DesignPost_costumer)
admin.site.register(bill,DesignPost_bill)


# Register your models here.
