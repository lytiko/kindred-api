from django.db import models

class Person(models.Model):

    class Meta:
        db_table = "people"
        verbose_name_plural = "people"
        ordering = ["last_name"]

    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, blank=True)
    met = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"