import subprocess
from django.http import HttpResponse
from django.shortcuts import render, redirect

def run_streamlit_app(request):
    # Replace 'path/to/prediction_app.py' with the actual path to your Streamlit app file.
    streamlit_command = ['streamlit', 'run', '/Users/dany/Documents/Fall 2023/Software Engineer/prediction.py']
    subprocess.Popen(streamlit_command)
    return HttpResponse("Hinton.io will open in a new tab...")

def index(request):
    return redirect('login')