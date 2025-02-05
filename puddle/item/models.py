from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",) # Alphabetic order
        verbose_name_plural = "Categories" # Pluralize Table name

    def __str__(self):
            return self.name       
