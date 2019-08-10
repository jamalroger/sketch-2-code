from django.conf.urls import url ,include
from app import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^doc2pdf/$', views.doc2pdf.as_view()),
    url(r'^sketchcode/$', views.sketchcode.as_view()),
    url(r'^contact/$', views.contact.as_view()),
    url(r'^support/$', views.support.as_view()),
    url(r'^google8bce582a947019d2.html$', views.google.as_view()),
     url(r'^ads.txt$', views.ads.as_view()),
]
