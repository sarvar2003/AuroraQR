import subprocess

# Home view
def home(request):
        
        cmd = 'python main.py'

        process = subprocess.Popen(cmd, shell=True)

        process.communicate()