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

class TblCustomer(models.Model):
    id = models.AutoField(primary_key=True)
    retail_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'tbl_customer'  # Map to the existing tbl_customer table
        managed = False  # Prevent Django from creating the table

    def __str__(self):
        return self.retail_name

class TblVendor(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    contract_period = models.CharField(max_length=50, null=True, blank=True)  # New field for contract period

    class Meta:
        db_table = 'tbl_vendor'  # Map to the existing tbl_vendor table
        managed = False  # Prevent Django from creating the table

    def __str__(self):
        return self.company_name
