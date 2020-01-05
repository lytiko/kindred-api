from django.db import models

class Tier(models.Model):

    class Meta:
        db_table = "tiers"
        ordering = ["level"]

    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    level = models.IntegerField(unique=True)

    def __str__(self):
        return self.name



class Category(models.Model):

    class Meta:
        db_table = "categories"
        verbose_name_plural = "categories"
        ordering = ["order"]

    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    order = models.IntegerField()

    def __str__(self):
        return self.name



class Person(models.Model):

    class Meta:
        db_table = "people"
        verbose_name_plural = "people"
        ordering = ["last_name"]

    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, blank=True)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"