from django.urls import path
from estimates.views import EstimateListView
 

urlpatterns = [
    path('', EstimateListView.as_view()),
]