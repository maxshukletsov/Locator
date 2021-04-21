from django.db import models
from Compaies.models import Compaies
from Devices.models import Devices
from django.db.models import JSONField


class Locations(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=5)
    longitude = models.DecimalField(max_digits=9, decimal_places=5)
    created_at = models.DateField(max_length=255, default=None, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, max_length=255, null=True, blank=True)
    company_id = models.ForeignKey(Compaies, related_name="compaies_loc", default=None, on_delete=models.CASCADE)
    device_id = models.ForeignKey(Devices, related_name="device_loc", default=None, on_delete=models.CASCADE)
    data = JSONField(default=dict)

    def __str__(self):
        return str(self.pk)
