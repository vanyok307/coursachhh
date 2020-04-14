from django.urls import path
from railway.views import TrainView,start_page,WayCreateView


urlpatterns = [
        path('',start_page,name='page1'),
        path('train/<int:id>/',TrainView.as_view(),name='railway'),
        path('way/create/',WayCreateView.as_view(),name='way_create'),
]
