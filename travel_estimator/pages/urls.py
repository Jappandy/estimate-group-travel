from django.urls import path

from .views import HomePageView
from estimates.views import EstimateListView
from estimates.views import CreateEstimateView, UpdateEstimateView

 

urlpatterns = [
    path('', EstimateListView.as_view(), name='home'),
    path('add-estimate-form/', CreateEstimateView.as_view(), name='add-estimate-form'),
    path('estimate-update-form/', UpdateEstimateView.as_view(), name='estimate-update-form'),
]

# urlpatterns = [
#     path('', HomePageView.as_view(), name='home'),
# ]