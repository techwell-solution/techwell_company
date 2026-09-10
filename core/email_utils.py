import resend
from django.conf import settings


def send_resend_email(to, subject, html):
    """
    Send an email using Resend.
    Returns the Resend response or None if no API key is configured.
    """

    if not settings.RESEND_API_KEY:
        print("RESEND_API_KEY is not configured.")
        return None

    resend.api_key = settings.RESEND_API_KEY

    response = resend.Emails.send({
        "from": settings.RESEND_FROM_EMAIL,
        "to": [to] if isinstance(to, str) else to,
        "subject": subject,
        "html": html,
    })

    return response