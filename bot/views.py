import subprocess
from django.views.generic import TemplateView
# Home view
# def home(request):
        
        # cmd = 'python main.py'

        # process = subprocess.Popen(cmd, shell=True)

        # process.communicate()
class HomeView(TemplateView):
        template_name = 'home.html'
