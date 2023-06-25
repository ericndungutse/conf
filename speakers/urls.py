from django.urls import path
from speakers import views

urlpatterns = [
    path('', views.speakers_view),
    path('create/', views.create_speaker_view),
    path('<id>/', views.speaker_view),
    path('<id>/update/', views.update_speaker_view),
    path('<id>/delete/', views.delete_speaker_view),
    path('<id>/delete/delete-confirm/', views.confirm_delete_view)
]
