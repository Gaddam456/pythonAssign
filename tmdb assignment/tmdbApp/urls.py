from django.urls import path
from .views import *
urlpatterns = [
    path('searchMovieName/', searchingMovieName),
    path('top100Movies/', top100Movies)
]
