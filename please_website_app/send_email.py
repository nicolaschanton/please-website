# -*- coding: utf-8 -*-

from django.core.mail import EmailMessage


def send_email(context, to_address, from_address, reply_to_address, subject, template):

    content = template.render(context)

    print(content)

    email = EmailMessage(
        subject=subject,
        body=content,
        from_email=from_address,
        to=[to_address],
        headers={'Reply-To': reply_to_address},
    )

    email.send()

    print(email)

    return
