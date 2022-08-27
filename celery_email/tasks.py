from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def birthday_message():
    send_mail(
        f'Birth Alert',
        "Happy birthday brother bros",
        settings.DEFAULT_FROM_EMAIL,
        ["vykeoj@gmail.com"],
        fail_silently=False,
    )
    print('email sent successfully')


 