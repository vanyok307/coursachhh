from django.urls import path
from railway.views import (TrainView, start_page,
                        WayView, StationView, TicketView)



urlpatterns = [
        path('',start_page,name='page1'),
        path('rail/<int:id>/',TrainView.as_view(),name='railway'),
        path('way/<int:id>/', WayView.as_view(), name='way'),
        path('way/create/', WayCreateView.as_view(), name='waycreate'),
        path('station/<int:id>/', StationView.as_view(), name='station'),
        path('station/create/', StationCreateView.as_view(), name='stationcreate'),
        path('ticket/<int:id>/', TicketView.as_view(), name='ticket'),
        path('ticket/create/', TicketCeateView.as_view(), name='ticketcreate'),
]
