from django.db import models
from django.utils import timezone

class Cabinet(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, verbose_name='Вендор')  
    model = models.CharField(max_length=200, blank=True, default='')
    width = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    height = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    resolution_w = models.IntegerField(default=0)
    resolution_h = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    brightness = models.IntegerField(default=0)
    module_w = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    module_h = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    module_res_w = models.IntegerField(default=0)
    module_res_h = models.IntegerField(default=0)
    power_max = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    power_typical = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    greyscale = models.IntegerField(default=0)
    refresh_rate = models.IntegerField(default=0)
    view_angle_hor = models.IntegerField(default=0)
    view_angle_vert = models.IntegerField(default=0)
    color_temp_min = models.IntegerField(default=0)
    color_temp_max = models.IntegerField(default=0)
    frame_frequency = models.IntegerField(default=0)
    lifespan = models.IntegerField(default=0)
    power_supply = models.CharField(max_length=200, blank=True, default='')
    ip_rating = models.CharField(max_length=200, blank=True, default='')
    working_temp = models.CharField(max_length=200, blank=True, default='')
    storage_temp = models.CharField(max_length=200, blank=True, default='')
    working_humidity = models.CharField(max_length=200, blank=True, default='')
    storage_humidity = models.CharField(max_length=200, blank=True, default='')
    pixel_pitch = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fob_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return self.model

class Vendor(models.Model):
    brand = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.brand