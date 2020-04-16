from django.urls import path
from railway.views import TrainView,WayView,StationView
from railway.views import TrainView,start_page,WayCreateView,StationCreateView,TicketCreateView
from railway.views import WayEditView,StationEditView
from django.views.generic.base import RedirectView

urlpatterns = [
        path('',start_page,name='page1'),
        path('admin/', RedirectView.as_view(url='/admin'), name="admin_panel"),
        path('train/<int:id>/',TrainView.as_view(),name='railway'),
        path('way/<int:id>/', WayView.as_view(), name='ways'),
        path('way/create/',WayCreateView.as_view(),name='way_create'),
        path('way/<int:id>/update/',WayEditView.as_view(),name='way_update'),
        path('station/<int:id>/',StationView.as_view(), name='stations'),
        path('station/create/',StationCreateView.as_view(),name='station_create'),
        path('station/<int:id>/update/',StationEditView.as_view(),name='station_update'),
        path('ticket/create/',TicketCreateView.as_view(),name='ticket_create'),
]
