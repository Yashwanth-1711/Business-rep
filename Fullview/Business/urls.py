
from django.urls import path
from .views import *


urlpatterns = [
    path('Country/', CountryAPIView.as_view(),name='country_api'),
    path('Country/<int:pk>/', CountryAPIView.as_view(),name='country_api_num'),
    path('State/', StateAPIView.as_view(),name='State_api'),
    path('City/', CityAPIView.as_view(),name='City_api'),
    path('Area/', AreaAPIView.as_view(),name='Area_api'),
    path('Department/', DepartmentListCreate.as_view(),name='Department_api'),
    path('Department/<int:pk>/', DepartmentRetrieveUpdateDelete.as_view(),name='Department_api_num'),
    path('Designation/', DesignationListCreate.as_view(),name='Designation_api'),
    path('Designation/<int:pk>/',DesignationRetrieveUpdateDelete.as_view(),name='Designation_api_num'),
    path('Employee/', EmployeeAPIView.as_view(),name='Employee_api'),
    path('Employee/<int:employeeID>/', EmployeeAPIView.as_view(),name='Employee_api_num'),
    path('toggle-status/<int:employee_id>/', toggle_employee_status, name='toggle_status'),
    path('Attendance/',AttendanceMenus1APIView.as_view(),name='Attendance'),
    path('Holiday/',HolidayAPIView.as_view(),name='Holiday'),
]

