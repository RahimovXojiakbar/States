from django.urls import path
from django.conf.urls import handler404
from main.views import (Page404View, 
                        states_view, 
                        state_detail_view, 
                        region_detail_view, 
                        district_detail_view, 
                        mfy_detail_view, 
                        neighborhood_detail_view, 
                        house_detail_view, 
                        human_detail_view)

handler404 = Page404View
urlpatterns = [
    path('', states_view, name='states_url'),
    path('state/<str:uuid>/', state_detail_view, name='state_detail_url'),
    path('region/<str:uuid>/', region_detail_view, name='region_detail_url'),
    path('district/<str:uuid>/', district_detail_view, name='district_detail_url'),
    path('mfy/<str:uuid>/', mfy_detail_view, name='mfy_detail_url'),
    path('neighborhood/<str:uuid>/', neighborhood_detail_view, name='neighborhood_detail_url'),
    path('house/<str:uuid>/', house_detail_view, name='house_detail_url'),
    path('human/<str:uuid>/', human_detail_view, name='human_detail_url'),

]
