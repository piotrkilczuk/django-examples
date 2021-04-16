from django.urls import path

from methods_in_templates.views import example

urlpatterns = [
    path('example/', example),
]
