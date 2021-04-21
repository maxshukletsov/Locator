from django.db import models


# Create your models here.
class Compaies(models.Model):
    company_token = models.CharField(max_length=255, null=True, default=None, blank=True)
    created_at = models.DateField(max_length=255, default=None, null=True, blank=True)
    updated_at = models.DateField(max_length=255, default=None, null=True, blank=True)

    def __str__(self):
        return self.company_token
