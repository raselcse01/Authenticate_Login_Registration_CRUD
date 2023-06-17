

from django.urls import path
from  .views import *

urlpatterns = [
 
    path('home/' ,INDEX, name='home'),
    path('add',ADD, name='add'),
    path('edit',EDIT, name='edit'),
    path('update/<str:id>',Update, name='update'),
    path('delete/<str:id>',Delete, name='delete'),
    path('Registion/',Registion,name='Registion'),
    path('login/',Login,name='login'),
    path('show/',EmployeeShow,name='show')

    
]
