from django_q.tasks import schedule, Schedule
from django.core.mail import send_mail
from .models import Alert
import requests

def check_price():
    response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    data = response.json()
    current_price = float(data['price'])
    
    alerts = Alert.objects.filter(status='created', target_price__lte=current_price)
    for alert in alerts:
        send_mail(
            'Price Alert',
            f'The price of Bitcoin has reached your target price of {alert.target_price}.',
            '796e07001@smtp-brevo.com',
            [alert.email],
            fail_silently=False,
        )
        alert.status = 'triggered'
        alert.save()

schedule(
    'alerts.tasks.check_price',
    schedule_type=Schedule.HOURLY  # Run every hour
)
