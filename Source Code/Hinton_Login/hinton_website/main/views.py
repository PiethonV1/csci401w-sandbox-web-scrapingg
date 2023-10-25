import subprocess
from django.http import HttpResponse
from django.shortcuts import render, redirect

def streamlit_view(request):
    user_name = request.user.username

    # Start the Streamlit app as a background process
    streamlit_command = [
        'streamlit', 'run',
        '/Users/danys/OneDrive/Documents/RIC/Fall 2023/CSCI 401W/csci401w-sandbox-web-scrapingg/Source Code/Hinton_Login/hinton_website/prediction.py'
    ]

    subprocess.Popen(streamlit_command)

    return render(request, 'streamlit_template.html', {'user_name': user_name})



def index(request):
    return redirect('login')