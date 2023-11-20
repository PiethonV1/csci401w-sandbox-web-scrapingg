# urls.py
from django.urls import path, include
from .views import get_tickers
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view-forecast/', views.streamlit_view, name='view-forecast'),
     path('get-username/', views.get_username, name='get-username'),
     path('api/tickers', get_tickers, name='get_tickers'),

]