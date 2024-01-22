from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.MusicianCreateView.as_view(), name='addMusician'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('edit/<int:id>', views.editMusicianView.as_view(), name='edit_musician'),
    path('delete/<int:id>', views.MusicianDeleteView.as_view(), name='delete_musician'),
    path('login/', views.MusicianLoginView.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('musician/<int:id>', views.MusicianProfileView.as_view(), name='musician'),
     
]
