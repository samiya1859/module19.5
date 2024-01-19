from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.MusicianCreateView.as_view(), name='addMusician'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('edit/<int:pk>', views.editMusicianView.as_view(), name='edit_musician'),
    path('delete/<int:pk>', views.MusicianDeleteView.as_view(), name='delete_musician'),
    path('login/', views.MusicianLoginView.as_view(), name='user_login'),
    path('logout/', views.MusicianLogoutView.as_view(), name='user_logout'),
    # path('musician/', views.MusicianLogoutView.as_view(), name='musician'),
     
]
