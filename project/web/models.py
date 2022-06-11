from django.db import models
from datetime import timedelta


# Create your models here.
class supplier(models.Model):
    name = models.CharField(max_length=40)
    number = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    account_Number = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class sparepart_order(models.Model):
    id_import = models.CharField(max_length=10,default="")
    supplier = models.ForeignKey(supplier, on_delete=models.CASCADE)
    price = models.FloatField()
    DateTime = models.DateTimeField('Date & Time')

    def __str__(self):
        return f'{self.supplier} {self.DateTime + timedelta(minutes=0)}'

    class Meta:
        verbose_name_plural = "Spareparts Orders"
        verbose_name = "Spareparts Order"

class sparepart(models.Model):
    id_code = models.CharField(max_length=30,default="")
    type = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    quantity = models.IntegerField()
    Price_Per_Unit = models.FloatField()
    Price_Per_Unit_Imp = models.FloatField(null=True)
    inventory = models.CharField(max_length=40,default="")

    def __str__(self):
        return f'{self.type} {self.model}'

class import_wait(models.Model):
    id_import = models.CharField(max_length=10, default="")
    sparepart = models.ForeignKey(sparepart, on_delete=models.CASCADE)
    supplier = models.ForeignKey(supplier, on_delete=models.CASCADE,default="")
    quantity = models.IntegerField()
    price = models.FloatField()
    DateTime = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Import Wait"
        verbose_name = "Import Wait"

    def __str__(self):
        return f'{self.sparepart}{" : "}{self.quantity}{" ชิ้น : "}{self.price}{" บาท "}{self.DateTime}'

class import_part(models.Model):
    id_import = models.CharField(max_length=10, default="")
    sparepart = models.ForeignKey(sparepart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    DateTime = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Import Parts"
        verbose_name = "Import Part"

    def __str__(self):
        return f'{self.sparepart}{" : "}{self.quantity}{" ชิ้น : "}{self.price}{" บาท "}{self.DateTime}'

class customer_car(models.Model):
    license = models.CharField(max_length=10)
    name = models.CharField(max_length=40,null=True,default="บิลเงินสด")
    number = models.CharField(max_length=10,null=True)

    class Meta:
        verbose_name_plural = "Customer Cars"
        verbose_name = "Customer Car"

    def __str__(self):
        return f'{self.license}'

class export_part(models.Model):
    id_bill = models.CharField(max_length=40, null=True ,default="")
    sparepart = models.CharField(max_length=40)
    quantity = models.IntegerField()
    price = models.FloatField()
    DateTime = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Export Parts"
        verbose_name = "Export Part"

    def __str__(self):
        return f'{self.sparepart}{" : "}{self.quantity}{" ชิ้น : "}{self.price}{" บาท "}{self.DateTime}'

class export_bill(models.Model):
    id_bill = models.CharField(max_length=10,default="")
    part_all = models.CharField(max_length=40,default="")

    def __str__(self):
        return f'{self.id_bill}'

class bill(models.Model):
    id_bill = models.ForeignKey(export_bill, on_delete=models.CASCADE, default="")
    customer_Car = models.ForeignKey(customer_car, on_delete=models.CASCADE)
    fixing_Charge = models.FloatField()
    sparepart_price = models.FloatField()
    total_Charge = models.FloatField()
    DateTime = models.DateTimeField('Date & Time')

    def __str__(self):
        return f'{self.id_bill}{" : "}{self.customer_Car}{" : "}{self.DateTime}'



# Create your models here.
