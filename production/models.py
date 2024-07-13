# from django.db import models

# class ProductionLine(models.Model):
#     name = models.CharField(max_length=100)

# class MaterialMaster(models.Model):
#     sku_code = models.CharField(max_length=100)
#     sku_desc = models.CharField(max_length=255)
#     sut = models.CharField(max_length=100)

# class Pallet(models.Model):
#     production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
#     process_order_number = models.IntegerField()
#     date = models.DateField()
#     sku_code = models.ForeignKey(MaterialMaster, on_delete=models.CASCADE)
#     batch_number = models.CharField(max_length=100)
#     process_order_qty = models.IntegerField()
#     bin_number = models.CharField(max_length=100)
#     pallet_qty = models.IntegerField()
#     transfer_order_number = models.CharField(max_length=100, unique=True)
#     status = models.CharField(max_length=50)
from django.db import models

class ProductionLine(models.Model):
    name = models.CharField(max_length=100)

class MaterialMaster(models.Model):
    sku_code = models.CharField(max_length=100)
    sku_desc = models.CharField(max_length=255)
    sut = models.CharField(max_length=100)

class Pallet(models.Model):
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    process_order_number = models.IntegerField()
    date = models.DateField()
    sku_code = models.ForeignKey(MaterialMaster, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=100)
    process_order_qty = models.IntegerField()
    bin_number = models.CharField(max_length=100, blank=True)
    pallet_qty = models.IntegerField()
    transfer_order_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=50, blank=True)
    capacity = models.FloatField()
# class Bin(models.Model):
#     bin_number = models.CharField(max_length=100, unique=True)
#     capacity = models.IntegerField()
#     current_load = models.IntegerField()

class Bin(models.Model):
    current_load = models.FloatField()
    capacity = models.FloatField()

