from django.urls import path
from . import views


urlpatterns = [
    path('getdetail/<str:slack_name>/<str:track_name>/', views.get_detail)
] 