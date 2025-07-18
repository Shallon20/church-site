from django.urls import path
from . import views
from core import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home, name="home"),
  path('about/', views.about, name="about"),
  path('ministries/', views.ministries, name="ministries"),
  path('ministry/', views.ministry, name="ministry"),
  path('contact/', views.contact, name="contact"),
  path('give/', views.give, name="give"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)