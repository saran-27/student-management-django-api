from django.urls import path
from .views import *

urlpatterns = [
    path('Rank/',RankApi.as_view()),
    path('Rank/<int:id>/', RankApi.as_view())

]