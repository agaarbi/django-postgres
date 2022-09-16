from django.db import models
import uuid
import bcrypt

# Create your models here.


class Accounts(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)

    def save(self, *args, **kwargs):
        password = str(self.password)
        password = password.encode('utf-8')
        self.password = bcrypt.hashpw(password, bcrypt.gensalt())
        # print(self.password)
        super(Accounts, self).save(*args, **kwargs)
