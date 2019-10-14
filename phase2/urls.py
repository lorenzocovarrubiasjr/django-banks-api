from django.urls import path 
from . import views  

urlpatterns = [
  path('api', views.api, name='api'),
  path('api/branches', views.api_branches, name='api_branches'),
  path('api/branches/<id>', views.api_branch, name='api_branch'),
  path('api/branches/new/<address>/<city>/<state>/<zipcode>', views.api_branch_new, name='api_branch_new'),
  path('api/branches/<id>/delete', views.api_branch_delete, name='api_branch_delete'),
  path('api/employees', views.api_employees, name='api_employees'),
  path('api/employees/new/<firstname>/<lastname>/<branch_id>/<position>/<start_date>', views.api_employee_new, name='api_employee_new'),
  path('api/employees/<id>/delete', views.api_employee_delete, name='api_employee_delete')
]