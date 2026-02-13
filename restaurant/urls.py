from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('booking/', views.BookingViewSet.as_view(), name='booking-list'),
    path('booking/<int:pk>/', views.SingleBookingView.as_view(), name='booking-detail'),
]
