from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name= 'home'),
    path('math_questions/', math_questions, name= 'math_questions'),
    path('answer/<int:i_id>/', answer, name= 'answer'),
    path('geo_questions/', geo_questions, name= 'geo_questions')
]