from django.urls import path
from . import views

urlpatterns = [
    path('', views.qm, name='qm-qm'),
    # path('submit/', views.submit, name='qm-submit'),
]