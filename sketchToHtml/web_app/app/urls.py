from django.conf.urls import url ,include
from app import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
