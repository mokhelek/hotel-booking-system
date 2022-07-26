from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Rooms)
admin.site.register(models.BookerDetails)
admin.site.register(models.Extras)
admin.site.register(models.RoomPictures)

