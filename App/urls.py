from django.urls import path
from knox import views as knox_views
from . import views
from django.urls import path

urlpatterns = [
    path('chart/<int:id>', views.graph, name='chart'),
    path('caster/', views.chart),
      
]