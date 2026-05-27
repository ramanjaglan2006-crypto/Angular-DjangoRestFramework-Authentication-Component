from django.dispatch import receiver
from django.core.mail import send_mail
from django_rest_passwordreset.signals import reset_password_token_created
from django.conf import settings

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Signal to send password reset email.
    """
    # In a real application, you would use a proper frontend URL
    email_plaintext_message = f"{settings.FRONTEND_URL}/confirm-password/?token={reset_password_token.key}"

    send_mail(
        subject=f"Password Reset for {settings.SITE_NAME}",
        message=email_plaintext_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[reset_password_token.user.email]
    )
