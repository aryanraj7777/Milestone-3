# payroll/utils.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

def send_payroll_email(payroll):
    user = payroll.user
    subject = 'Your Payroll for {} has been released!'.format(payroll.created_at.strftime('%B'))
    template = get_template('payroll/email.html')
    context = Context({'user': user, 'payroll': payroll, 'month': payroll.created_at.strftime('%B')})
    content = template.render(context)
    email = EmailMultiAlternatives(subject, content, 'your_organization_email@example.com', [user.email])
    email.attach_alternative(content, 'text/html')
    email.send()
