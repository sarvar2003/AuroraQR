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
    template_name = 'Home/home.html'

class HelpView(TemplateView):
    template_name = 'Home/help.html'


