from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('send-message/', views.send_message, name='send_message'),
    path('api/portfolio/', views.api_portfolio_data, name='api_portfolio'),
]
