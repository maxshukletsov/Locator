from django.db import models
from Compaies.models import Compaies


# Create your models here.
class Devices(models.Model):
    company_id = models.ForeignKey(Compaies, related_name="compaies_dev", default=None, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=255, null=True, default=None, blank=True)
    device_model = models.CharField(max_length=255, null=True, default=None, blank=True)
    created_at = models.DateField(max_length=255, default=None, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, max_length=255, null=True, blank=True)
    app = models.CharField(max_length=255, null=True, default=None, blank=True)
    version = models.CharField(max_length=255, null=True, default=None, blank=True)

    def __str__(self):
        return self.device_id
