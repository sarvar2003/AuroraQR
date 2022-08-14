import threading
from django.views.generic import TemplateView

from .telegramBot import *


def setupBotThread():
    """
    Setup the thread for running the bot in background 
    """

    botThread = threading.Thread(target=main)
    
    botThread.start()
    

class HomeView(TemplateView):
    setupBotThread()
    template_name = 'bot/home.html'


