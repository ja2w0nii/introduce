from django.db import models


# Create your models here.
class AccessLogModel(models.Model):
    class Meta:
        db_table = "AccessLog"

    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=256)
