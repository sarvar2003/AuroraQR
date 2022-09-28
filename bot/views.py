import time
import threading
from django.views.generic import TemplateView
import requests
import schedule


from .telegramBot import *

def setupBotThread():
    """
    Setup the thread for running the bot in background 
    """

    botThread = threading.Thread(target=main)
    
    botThread.start()
    

def sendRequest():
    requests.get('https://aurora-qr.herokuapp.com/')

def keepServerAlive():
    schedule.every(20).minutes.do(sendRequest)

    while True:
        schedule.run_pending()
        time.sleep(1)



class HomeView(TemplateView):
    setupBotThread()
    keepServerAlive()
    template_name = 'Home/home.html'


class HelpView(TemplateView):
    template_name = 'Home/help.html'


