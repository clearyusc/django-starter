from django.contrib.auth.models import AbstractUser
from django.db import models


class PaymentInfo():
    pass

class CustomUser(AbstractUser):
    '''payment_info = models.ForeignKey(
        PaymentInfo,
        on_delete=models.CASCADE,
    )'''
    pass

