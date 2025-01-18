from django.urls import path
from . import views

urlpatterns = [
    path('', views.states_view, name='states_url'),
    path('state/<str:uuid>/', views.state_detail_view, name='state_detail_url'),
    path('region/<str:uuid>/', views.region_detail_view, name='region_detail_url'),
    path('district/<str:uuid>/', views.district_detail_view, name='district_detail_url'),
    path('mfy/<str:uuid>/', views.mfy_detail_view, name='mfy_detail_url'),
    path('neighborhood/<str:uuid>/', views.neighborhood_detail_view, name='neighborhood_detail_url'),
    path('house/<str:uuid>/', views.house_detail_view, name='house_detail_url'),
    path('human/<str:uuid>/', views.human_detail_view, name='human_detail_url'),

]
