#models
from django.db import models
#
from django.db.models import Count

class ReunionManager(models.Manager):
    def cantidad_reunions_job(self):
        result = self.values('person__job').annotate(
            cantidad = Count('id')
        )
        return result