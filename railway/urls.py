from django.urls import path
from railway.views import TrainView,start_page


urlpatterns = [
        path('',start_page,name='page1'),
        path('rail/<int:id>',TrainView.as_view(),name='railway'),
]
