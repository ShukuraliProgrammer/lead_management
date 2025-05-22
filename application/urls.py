from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApplicationListView.as_view(), name="list"),
    path('<int:pk>/', views.ApplicationUpdateView.as_view(), name="detail"),
    path('submit/', views.ApplicationSubmitView.as_view(), name='application-submit'),
]