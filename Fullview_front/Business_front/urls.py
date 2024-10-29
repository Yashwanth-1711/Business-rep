from django.urls import path
from .views import *


urlpatterns = [
    path("Home/",Home, name='Home' ),
    path('Master/', Master, name='Master'),
    path('createcountry/',createcountry,name="Country"),
    path('edit_country/',editbutton,name='edit_country'),
    path('delete_country/', deleteButton,name='delete_country'),
    path('createstate/',createstate,name='State'),
    path('edit_state/',editbuttonstate,name='edit_state'),
    path('delete_state/', deleteButtonstate,name='delete_state'),
    path('createcity/',createcity,name='City'),
    path('edit_city/',editbuttoncity,name='edit_city'),
    path('delete_city/', deleteButtoncity,name='delete_city'),
    path('createarea/',createarea,name='Area'),
    path('edit_area/',editbuttonarea,name='edit_area'),
    path('delete_area/', deleteButtonarea,name='delete_area'),
    path('createdepartment/',createdepartment,name='Department'),
    path('edit_department/',editbuttondepartment,name='edit_department'),
    path('delete_department/', deleteButtondepartment,name='delete_department'),
    path('createdesignation/',createdesignation,name='Designation'),
    path('edit_designation/',editbuttondesignation,name='edit_designation'),
    path('delete_designation/', deleteButtondesignation,name='delete_designation'),
    path('createemployee/',createemployees,name='Employee'),
    path('createemployee/<int:employee_id>/',createemployees,name='Employee_num'),
    path('edit_employee/',editEmployee,name='edit_employee'),
    path('delete_employee/',deleteEmployee,name='delete_employee'),
    path('Employee_List/',EmployeeFullList,name="Employee_list"),
    path('Human-resourses/',Human_resources,name="Human_Resourses"),
    path('createattendance/',createattendance,name="Attendance"),
    path('edit_attendance/',editAttendance,name="edit_attendance"),
    path('Attendance_sheet/',Attendance_Sheet,name="Attendance_sheet"),
    path('Holiday/',createholiday,name="Holiday"),
    path('delete_holiday/',deleteButtonholiday,name="delete_holiday"),

    
]
