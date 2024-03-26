"""
URL configuration for machinetest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.views.generic import RedirectView
from .views import ClientListCreateView, ClientRetrieveUpdateDestroyView, ProjectListCreateView, ProjectRetrieveUpdateDestroyView

urlpatterns = [
    # Redirect empty path to 'clients/'
    path('', RedirectView.as_view(url='clients/', permanent=False)),

    # Include your app's URL patterns
    path('clients/', include([
        # Clients URLs
        path('', ClientListCreateView.as_view(), name='client-list-create'),
        path('<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-retrieve-update-destroy'),

        # Projects URLs
        path('<int:pk>/projects/', ProjectListCreateView.as_view(), name='project-list-create'),
        path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-retrieve-update-destroy'),
    ])),
]

