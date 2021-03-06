from django.db import models
from datetime import datetime
import os
# Create your models here.

# def filepath(request, filename):
#     old_filename = filename
#     timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
#     filename = "%s-%s" % (timeNow, old_filename)
#     return os.path.join('uploads/', filename)

class accounts(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField(max_length=3)
    address = models.CharField(max_length = 100)
    mobile = models.IntegerField(max_length=11)
    email=models.EmailField(max_length=30)
    password = models.CharField(max_length = 20)
    confirm_password = models.CharField(max_length = 20)
    created_at = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table = 'users'

    def isExists(self):
        if accounts.objects.filter(email=self.email):
            return True
        return False

class msgs(models.Model):
    person_name = models.CharField(max_length=20)
    person_email = models.CharField(max_length=20)
    person_contact = models.IntegerField(max_length=11)
    msg = models.CharField(max_length=1000)