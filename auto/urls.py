from django.contrib import admin
from django.urls import path
from .views import HomeView,MahsulotView,ExtiyotQismQushishView,QismEditView,QismDeleteView,DownloadToExcel,CarDetailView,AvtoDeleteView,AvtoEditView,AvtoQushishView




urlpatterns = [
    path('', HomeView.as_view(), name='home'),    
    path('mahsulot/',MahsulotView.as_view(),name='mahsulot'),
    path('addmahsulot/',ExtiyotQismQushishView.as_view(),name='addmahsulot'),
    path('edit/extiyotqism/<id>/',QismEditView.as_view(),name='qismedit'),
    path('delete/extiyotqism/<int:id>/', QismDeleteView.as_view(), name='qismdelete'),
    path('export-to-excel/', DownloadToExcel.as_view(), name='export-to-excel'),
    path('car-detail/<id>/',CarDetailView.as_view(),name='car-detail'),
    path('addcar/',AvtoQushishView.as_view(),name='addcar'),
    path('edit/avto/<id>/',AvtoEditView.as_view(),name='avtoedit'),
    path('delete/avto/<id>/',AvtoDeleteView.as_view(),name='avtodelete'),
]
