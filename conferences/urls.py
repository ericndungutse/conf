from django.urls import path
from conferences import views

urlpatterns = [
    path('', views.conferences_view),
    path('create/', views.create_conference_view),
    path('<id>/', views.conference_view),
    path('<id>/update/', views.update_conference_view),
    path('<id>/delete/', views.delete_conference_view),
    path('<id>/delete/delete-confirm/', views.confirm_delete_view)
]
