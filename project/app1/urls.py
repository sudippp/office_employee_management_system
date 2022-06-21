from . import views
from django.urls import path

urlpatterns = [
    path('ibase', views.base, name='base'),
    path('ioffice', views.home, name='home'),
    path('accounts/manager_register', views.manager_register, name='manager_register'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('all_emp', views.all_emp, name='all_emp'),
    path('remove_emp', views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_emp'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
    path('update_emp', views.update_emp, name='update_emp'),
]
