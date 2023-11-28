# urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view-forecast/', views.streamlit_view, name='view-forecast'),
     path('get-username/', views.get_username, name='get-username'),

]