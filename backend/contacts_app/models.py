from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=25, null=True)
    zip = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=12, default="xxx-xxx-xxxx")
    email = models.EmailField(null=True)
    note = models.TextField()
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
