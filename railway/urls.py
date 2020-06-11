from django.urls import path
from railway.views import (TrainView,WaysView,
                           WayView,StationView,
                           logout_view)
from railway.views import (TrainView,start_page,
                           WayCreateView,StationCreateView, 
                           TicketsView,TicketFilterView, 
                           download, UserView,UserRegView,
                           TicketFilterStationView)

from railway.views import WayEditView,StationEditView
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('',start_page,name='page1'),
        path('login/', UserView.as_view(), name="user_log"),
        path('signup/', UserRegView.as_view(), name="user_reg"),
        path('redirect_to_sign_up/', RedirectView.as_view(url="/signup/"),name="sign"),
        path('admin/', RedirectView.as_view(url='/admin'), name="admin_panel"),
        path('logout/', logout_view, name="logout"),
        path('train/<int:id>/',TrainView.as_view(),name='railway'),
        path('way/', WaysView.as_view(), name='way_list'),
        path('way/create/',WayCreateView.as_view(),name='way_create'),
        path('way/<int:id>/', WayView.as_view(), name='way'),
        path('way/<int:id>/update/',WayEditView.as_view(),name='way_update'),
        path('station/<int:id>/',StationView.as_view(), name='stations'),
        path('station/<int:id>/update/',StationEditView.as_view(),name='station_update'),
        path('ticket/',TicketsView.as_view(),name='tickets'),
        path('ticket/<str:destination>/',TicketFilterView.as_view(),name='ticket_filter'),
        path('download/<str:id>/', download, name="download"),
        ]
