from django.urls import path

from landing.app.views import index, landing, stats

urlpatterns = [
    path('', index, name='index'),
    path('landing/', landing, name='landing'),
    path('stats/', stats, name='stats'),
]
