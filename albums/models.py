from django.db import models
from musicians  .models import MusicianModel
# Create your models here.

class AlbumModel(models.Model):
    AlbumName = models.CharField(max_length=20)
    MusicianName = models.ForeignKey(MusicianModel,on_delete=models.CASCADE)
    releaseDate = models.DateField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)])

    def __str__(self) :
        return self.AlbumName
