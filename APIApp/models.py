from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Client(models.Model):
    ClientName = models.CharField(max_length=50)

    def __str__(self):
        return self.ClientName

class Address(models.Model):
    rua = models.CharField(max_length=25)
    cidade = models.CharField(max_length=25)
    estado = models.CharField(max_length=25)
    CEP = models.CharField(max_length=15)
    pais = models.CharField(max_length=15)

    def __unicode__(self):
        return self.rua + ", " + self.cidade + ", "+ self.estado + ", " + self.CEP + ", " + self.pais

class User(models.Model):
    UserName = models.CharField(max_length=20)
    mainaddress = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='+')
    address = models.ManyToManyField(Address, verbose_name="list of addresses",related_name='+')
    client = models.OneToOneField(Client, related_name='+', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.UserName

### Autenticação por Token gerado automaticamente ###

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

for user in User.objects.all():
    Token.objects.get_or_create(user=user)

    

    
