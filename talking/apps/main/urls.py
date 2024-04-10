from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name="index"),
    path('talk/<str:room_name>', views.talk, name="talk"),
]