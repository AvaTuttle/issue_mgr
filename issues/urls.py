from django.urls import path
from . import views

urlpatterns = [
    path('', views.IssueListView.as_view(), name='issue_list'), 
    path('create/', views.issue_create, name='issue_create'),
    path('<int:pk>/', views.IssueDetailView.as_view(), name='issue_detail'),
    path('<int:pk>/update/', views.IssueUpdateView.as_view(), name='issue_update'),
]
