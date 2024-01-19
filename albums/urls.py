from django.urls import path
from . import views
urlpatterns = [
    path('addalbum/',views.AddAlbumView.as_view(),name='add_album'),
    path('editalbum/<int:id>/',views.EditAlbumView.as_view(),name='edit_album'),
    path('deletealbum/<int:id>/',views.DeleteAlbumView.as_view(),name='delete_album'),
    path('detailalbum/<int:id>/',views.AlbumDetailView.as_view(),name='detail_album'),
]
