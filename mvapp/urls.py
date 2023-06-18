from django.urls import path
from . import views
app_name='mvapp'
urlpatterns = [
    path('',views.f1,name='f1'),
    path('movie/<int:id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]