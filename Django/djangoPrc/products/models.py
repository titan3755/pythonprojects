from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=300, default='Enter the title here', blank=False)
    desc = models.TextField(default='Enter the description here')
    summary = models.TextField(default='Enter the summary here', blank=True, null=False)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    featured = models.BooleanField()

    def __str__(self):
        return self.title
