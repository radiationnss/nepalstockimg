from django.db import models
from stockimage.image_process import water_mark



class Image(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()
    image       = models.ImageField(upload_to='stockimages', blank=True, null=True)
    price       = models.DecimalField(max_digits=5, default=0, decimal_places=0)
    uploaded_by = models.CharField(max_length=100)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.image = water_mark(self.image)
        super().save(*args, **kwargs)
