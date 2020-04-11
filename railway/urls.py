from django.urls import path
from .views import TrainView,start_page


urlpatterns = [
        path('',start_page,name='page1'),
        path('rail/',TrainView.as_view(),name='railway'),
]
