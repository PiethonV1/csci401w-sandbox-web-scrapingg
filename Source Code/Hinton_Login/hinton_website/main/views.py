import subprocess
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse

def get_username(request):
    if request.user.is_authenticated:
        username = request.user.username
        return JsonResponse({"username": username})
    else:
        return JsonResponse({"error": "User is not authenticated"})

def streamlit_view(request):
    user_name = request.user.username

    # Start the Streamlit app as a background process
    streamlit_command = [
    'streamlit', 'run',
    '/Users/danys/OneDrive/Documents/RIC/Fall 2023/CSCI 401W/csci401w-sandbox-web-scrapingg/Source Code/Hinton_Login/hinton_website/prediction.py',
    # Have streamlit open in streamlit_template without opening on a new tab
    '--server.headless',
    '--server.runOnSave',
]
    subprocess.Popen(streamlit_command)

    return render(request, 'streamlit_template.html', {'user_name': user_name})

def index(request):
    return redirect('/login')