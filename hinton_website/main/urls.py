# urls.py
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run-streamlit-app/', views.run_streamlit_app, name='run-streamlit-app'),
]