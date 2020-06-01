
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'portfolio-home'),
    path('business/', views.business, name = 'business-home'),
    path('blog/', views.blog, name = 'blog-home'),
]
