from django.http import HttpResponse
import subprocess
from django.views.generic import TemplateView


def runFile():
    cmd = 'python bot/telegramBot.py'
    process = subprocess.Popen(cmd, shell=True)
    _, _ = process.communicate()

class HomeView(TemplateView):
    runFile()
    template_name = 'bot/home.html'


