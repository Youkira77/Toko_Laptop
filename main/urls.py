from django.urls import path
from . import views

app_name = 'main'

# URL patterns for main app
urlpatterns = [
    path('', views.index, name='index'),
    # Laporan pembelian view
    path('laporan/', views.laporan_pembelian, name='laporan_pembelian'),
    # Laptop list view
    path('laptops/', views.laptop_list, name='laptop_list'),
    path('pembeli/', views.pembeli_list, name='pembeli_list'),
    path('membeli/', views.membeli_detail, name='membeli_detail'),
    path('membeli/<int:pk>/', views.membeli_detail, name='membeli_detail_pk'),
]

