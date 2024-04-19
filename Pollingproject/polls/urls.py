from django.urls import path
from . import views
from .views import register, user_login,logout_view

from django.contrib import admin

# The path module is used to create the url patterns for the application
# to map the urls to the views
from django.urls import path

# The settings module is used to import the settings from the settings.py file
# to get the media, static files and other settings
from django.conf import settings

# The static module is used to import the static files from the settings.py file
from django.conf.urls.static import static



app_name = 'polls'
urlpatterns = [
	path('', views.index, name ='index'),
	path('<int:question_id>/', views.detail, name ='detail'),
	path('<int:question_id>/results/', views.results, name ='results'),
	path('<int:question_id>/vote/', views.vote, name ='vote'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
	path('logout/', logout_view, name='logout'),
]

    

