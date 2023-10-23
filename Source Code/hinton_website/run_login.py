import os
import subprocess
import streamlit as st

def run_server():
    virtualenv_path = 'myenv/bin/activate'  # Replace with the actual path
    django_project_path = '/hinton_website'  # Replace with the actual path

    # Activate the virtual environment
    activate_command = f'source {virtualenv_path}/bin/activate'
    subprocess.run(activate_command, shell=True, executable="/bin/bash")

    # Change to the Django project directory
    os.chdir(django_project_path)

    # Run the Django development server
    runserver_command = 'python manage.py runserver'
    subprocess.Popen(runserver_command, shell=True, executable="/bin/bash")

def main():
    st.title("Run Django Server")
    st.write("Click the button to run your Django server.")
    
    if st.button("Run Django Server"):
        run_server()

if __name__ == '__main__':
    main()
