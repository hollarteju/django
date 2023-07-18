from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path("next_page/<str:pk>", views.next_page, name="next_page")

]