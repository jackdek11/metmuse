from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=180)

    class Meta:
        db_table = 'metmuse.departments'

    def __str__(self):
        return self.name
