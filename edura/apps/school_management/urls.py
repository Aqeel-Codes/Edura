from django.urls import path
from . import views  
from django.http import HttpResponse

app_name = 'school_management'

urlpatterns = [
    
    path('list/', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('<uuid:pk>/edit/', views.student_edit, name='student_edit'),
    path('<uuid:pk>/delete/', views.student_delete, name='student_delete'),



    
    
]
