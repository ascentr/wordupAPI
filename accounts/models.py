# from django.db import models

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    #email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    #email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-confirm'), reset_password_token.key)
    email_plaintext_message = "{}?token={}".format('http://127.0.0.1:3000/newpassword' , reset_password_token.key)
    reset_url = email_plaintext_message

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Password Reset for Wordup Dictionary"),
        # message:         
        reset_url,
        # from:
        "noreply@ascentrick.com",
        # to:
        [reset_password_token.user.email]
    )

# Create your models here.
