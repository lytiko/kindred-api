from django.db import models

class Tier(models.Model):

    class Meta:
        db_table = "tiers"
        ordering = ["level"]

    name = models.CharField(max_length=256)
    level = models.IntegerField(unique=True)



class Category(models.Model):

    class Meta:
        db_table = "categories"
        ordering = ["order"]

    name = models.CharField(max_length=256)
    order = models.IntegerField()



class Person(models.Model):

    class Meta:
        db_table = "people"
        ordering = ["last_name"]

    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)