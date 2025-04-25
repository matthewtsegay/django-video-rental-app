from django.contrib import admin
from .models import Movie,Genre

class GenreAdmin(admin.ModelAdmin):
    
    list_display = ('id','name')
 
class MovieAdmin(admin.ModelAdmin): 
     list_display = ('genre','title','number_in_stoke','daily_rate')  
     
      
admin.site.register(Movie,MovieAdmin)
admin.site.register(Genre,GenreAdmin)
