import subprocess
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
import os
import time

def get_username(request):
    if request.user.is_authenticated:
        username = request.user.username
        return JsonResponse({"username": username})
    else:
        return JsonResponse({"error": "User is not authenticated"})

def is_streamlit_running():
    # Check if Streamlit is running by attempting to connect to it
    try:
        import requests
        response = requests.get("http://localhost:8501")
        return response.status_code == 200
    except:
        return False

def streamlit_view(request):
    user_name = request.user.username

    # Get the directory of the current Python script (the view)
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the relative path to your Streamlit script
    script_filename = "prediction.py"
    script_path = os.path.join(current_directory, script_filename)

    if not is_streamlit_running():
        # Start Streamlit as a background process
        streamlit_command = [
            'streamlit', 'run',
            script_path,  # Use the dynamically constructed relative path
            '--server.headless', 'true',  # Enable headless mode
            '--server.runOnSave', 'true',
            '--server.allowRunOnSave', 'true'
        ]
        subprocess.Popen(streamlit_command)

        # Wait for Streamlit to start (adjust the timeout as needed)
        max_wait_time = 60  # Maximum wait time in seconds
        start_time = time.time()
        while not is_streamlit_running() and (time.time() - start_time) < max_wait_time:
            time.sleep(1)

    return render(request, 'streamlit_template.html', {'user_name': user_name})

def index(request):
    return redirect('/login')
