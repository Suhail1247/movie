from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [
    path('',views.f1,name='f1'),
    path('movie/<int:movie_id>/',views.detail,name='detail')

]