from django.contrib import admin
from django.urls import path,include
from .views import CustomerView,ProductView,FileUploadView,CustomerDetailView

urlpatterns = [
    path('customers/',CustomerView.as_view()),
    path('add/',ProductView.as_view()),
    path('upload/',FileUploadView.as_view()),
    path('details/<int:id>/',CustomerDetailView.as_view())
]