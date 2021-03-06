from django.urls import path
from .views import index, student_list, student_add, student_update

urlpatterns = [
    path('', index, name='home'),
    path('list/', student_list, name='list'),
    path('add/', student_add, name='add'),
    path('update/<int:id>', student_update, name='update'),
]