from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    age = models.IntegerField()
    rfc = models.CharField(max_length=200)
    photoUrl = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class UserAddress(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    street = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=5)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.street