from django.urls import path
from . import views

urlpatterns = [
    # URLs for rendering templates
    path('', views.homepage, name='home'),

    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('departments/create/', views.department_create, name='department_create'),

    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('employee/<int:pk>/update/', views.employee_update, name='employee_update'),

    path('leave-requests/', views.leaverequest_list, name='leaverequest_list'),
    path('leave-requests/<int:pk>/', views.leaverequest_detail, name='leaverequest_detail'),
    path('leave-requests/create/', views.leaverequest_create, name='leaverequest_create'),

    # URLs for API endpoints
    path('api/departments/', views.DepartmentListCreateAPIView.as_view()),
    path('api/departments/<int:pk>/', views.DepartmentRetrieveUpdateDestroyAPIView.as_view()),

    path('api/employees/', views.EmployeeListCreateAPIView.as_view()),
    path('api/employees/<int:pk>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),

    path('api/leave-requests/', views.LeaveRequestListCreateAPIView.as_view()),
    path('api/leave-requests/<int:pk>/', views.LeaveRequestRetrieveUpdateDestroyAPIView.as_view()),
]
