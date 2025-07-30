from django.urls import path
from . import views

app_name='movies'

urlpatterns=[
        path('',views.index,name='index'),
        path('addpage/',views.addvideo,name='addvideo'),
        path('<int:video_id>/update/',views.updatevideo,name='updatevideo'),
        path('delete/<int:video_id>/',views.deletevideo,name='deletevideo'),
        path('<int:movie_id>',views.detail,name="detail")
]