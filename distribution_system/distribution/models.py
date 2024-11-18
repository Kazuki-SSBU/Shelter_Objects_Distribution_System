from django.db import models

class RequestAdress(models.Model):
    address = models.CharField(max_length=100, verbose_name="避難所の住所")
    
    def __str__(self):
        return self.address

class RequestData(models.Model):
    address = models.ForeignKey(RequestAdress, on_delete=models.CASCADE, verbose_name="避難所の住所")
    category = models.CharField(max_length=20, verbose_name="カテゴリ") 
    item_name = models.CharField(max_length=30, verbose_name="物資名")
    request_num = models.IntegerField(verbose_name="必要個数")
    stock_num = models.IntegerField(verbose_name="残存数")
    #address = models.CharField(max_length=100, verbose_name="避難所の住所")
    name = models.CharField(max_length=20, verbose_name="名前")
    distributed_num = models.IntegerField(default=0, verbose_name="配分決定済み個数")

    def __str__(self):
        return f"{self.item_name}:{self.request_num}"
# Create your models here.

# test

class StoreAdress(models.Model):
    address = models.CharField(max_length=100, verbose_name="倉庫住所")
    
    def __str__(self):
        return self.address

class StoreData(models.Model):
    address = models.ForeignKey(StoreAdress, on_delete=models.CASCADE, verbose_name="倉庫住所")
    category=models.CharField(max_length=20, verbose_name="カテゴリ")
    item_name = models.CharField(max_length=30, verbose_name="商品名")
    stock_num = models.IntegerField(verbose_name="在庫数")
    #address = models.CharField(max_length=100, verbose_name="倉庫住所")
    latitude = models.IntegerField(verbose_name="緯度")
    longitude = models.IntegerField(verbose_name="経度")
    
    def __str__(self) -> str:
        return f"{self.item_name}:{self.stock_num}"