from background_task import background
from django.contrib.auth.models import User

@background(schedule=5)
def notify_user():
    print('hello por favor')