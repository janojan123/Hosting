# myapp/models.py
from django.db import models

class TblUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'tbl_user'  # Map to the existing tbl_user table
        managed = False  # Prevent Django from creating the table

    def __str__(self):
        return self.username
