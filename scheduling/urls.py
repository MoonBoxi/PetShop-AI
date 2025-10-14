from django.urls import path
from . import views

app_name = 'scheduling'

urlpatterns = [
    path('services/', views.service_list, name='service_list_all'),
    path('services/<int:service_type_id>/', views.service_list, name='service_list_by_type'),
    path('select_date/<int:service_id>/', views.select_date, name='select_date'),
    path('select_time_slot/<int:service_id>/<str:date>/', views.select_time_slot, name='select_time_slot'),
    path('book_service/<int:service_id>/<int:time_slot_id>/', views.book_service, name='book_service'),
    path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]