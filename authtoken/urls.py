from django.urls import path

from .views import (
    OrganizationListCreateView,
    OrganizationDetailView,
    UserListCreateView,
    UserDetailView,
   
)
urlpatterns = [
    path('organizations/', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
   
]
