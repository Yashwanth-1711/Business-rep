

import json
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .Serializers import *

# Create your views here.

class CountryAPIView(APIView):
    message =""
    def post(self, request):
        data = request.data
        country_name = data.get('Country_name')

        # Check for duplicates
        if Country.objects.filter(Country_name__iexact=country_name).exists():
            return Response({"message": f"Country '{country_name}' already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Pass data to the serializer
        serializer = CountrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"Country '{country_name}' added successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            instance = Country.objects.get(id=pk)
            serializer = CountrySerializer(instance)
        else:
            countries = Country.objects.all()
            serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = Country.objects.get(id=pk) 
        serializer = CountrySerializer(instance, data=request.data) 
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully updated the country', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(Self,request,*args, **kwargs):
        pk = kwargs.get('pk')
        instance = Country.objects.get(id = pk)
        instance.delete()
        return Response({'message': 'The message is deleted'},status=status.HTTP_200_OK)


class StateAPIView(APIView):
    message =""
    def post(self, request):
        data = request.data
        state_code = data.get('State_code')
        state_name = data.get('State_name')
        country_name = data.get('State_Country')

        # Check for duplicates
        if State.objects.filter(State_name__iexact=state_name, State_Country__Country_name__iexact=country_name).exists():
            return Response({"message": f"State '{state_name}' already exists in Country '{country_name}'"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Pass data to the serializer
        
        serializer = StateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"State '{state_name}' added successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
    def get(self,request):
        stateID = request.query_params.get('stateID')
        if stateID:
            instance = State.objects.get(id=stateID)
            serializer=StateSerializer(instance)
        else:    
            states = State.objects.all()
            serializer = StateSerializer(states,many=True)

        return Response(serializer.data)
        
    def put(self,request):
        updateID = request.query_params.get("hiddenID")
        print(updateID,"ksksksksksk")
        instance = State.objects.get(id=updateID) 
        serializer = StateSerializer(instance, partial = True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":f" State is Updated Successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':serializer._errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(Self,request):
        stateID = request.query_params.get('stateID')
        instance = State.objects.get(id = stateID)
        instance.delete()
        return Response({'message': 'The message is deleted'},status=status.HTTP_200_OK)


class CityAPIView(APIView):
    def post(self, request):
        data = request.data
        Country_name = data.get('City_Country')
        State_name = data.get('City_State')
        City_name = data.get('City_name')

        # Check for duplicates
        if City.objects.filter(City_Country__Country_name__iexact=Country_name, City_State__State_name__iexact=State_name, City_name__iexact=City_name).exists():
            return Response({"message": f"In this Country '{Country_name}', the state '{State_name}' and the city '{City_name}' already exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Pass data to the serializer
        serializer = CitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"City '{City_name}' added successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
 
    def get(self,request):
        cityID = request.query_params.get('cityID')
        if cityID:
            instance = City.objects.get(id=cityID)
            serializer=CitySerializer(instance)
        else:    
            cities = City.objects.all()
            serializer = CitySerializer(cities,many=True)

        return Response(serializer.data)    

    def put(self,request):
        updateID = request.query_params.get('hiddenID')
        instance = City.objects.get(id = updateID)
        serializer = CitySerializer(instance, partial=True ,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data,"message":f" City'{City.City_name}' is Updated Successfully"},status=status.HTTP_200_OK)
        else:
            return Response({},status=status.HTTP_400_BAD_REQUEST) 


    def delete(self,request,):
        cityID = request.query_params.get('cityID')
        instance = City.objects.get(id = cityID)
        instance.delete()
        return Response({'message': "City is Successfully deleted"},status=status.HTTP_200_OK)

class AreaAPIView(APIView):
    def post(self,request):
        data = request.data
        Country_name = data.get('Area_Country')
        State_name = data.get('Area_State')
        City_name = data.get('Area_City')
        Area_name = data.get('Area_name')

        if Area.objects.filter(Area_Country__Country_name__iexact=Country_name, Area_State__State_name__iexact=State_name, Area_City__City_name__iexact=City_name, Area_name__iexact = Area_name).exists():
            return Response({"message": f"In this Country '{Country_name}',in the state '{State_name}'in this city '{City_name}'  and the Area is '{Area_name}' already exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = AreaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"City '{Area_name}' added successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    def get(self,request):
        areaID = request.query_params.get('areaID')
        if areaID:
            instance = Area.objects.get(id = areaID)
            serializer = AreaSerializer(instance)
        else:
            Areas = Area.objects.all()
            serializer = AreaSerializer(Areas,many = True)
        return Response(serializer.data)    

    def put(self,request):
        updateID = request.query_params.get('hiddenID')
        instance = Area.objects.get(id = updateID)
        serializer = AreaSerializer(instance, partial = True ,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":f"Area is Updated Successfully"},status=status.HTTP_200_OK)
        else:
            return Response({},status=status.HTTP_400_BAD_REQUEST) 


    def delete(self,request):
        areaID = request.query_params.get('areaID')
        instance = Area.objects.get(id = areaID)
        instance.delete()
        return Response({'message': "Area is Successfully deleted"},status=status.HTTP_200_OK)
    



class DepartmentListCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'pk'  
     





class DesignationListCreate(generics.ListCreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class DesignationRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    lookup_field = 'pk'  




class EmployeeAPIView(APIView):
    
    def generate_employee_code(self):
        last_employee = Employee.objects.order_by('id').last()
        if not last_employee:
            return "EMP0001"

        last_code = last_employee.Employee_Code
        new_code = int(last_code.replace('EMP', '')) + 1
        new_employee_code = f"EMP{new_code:04d}"
        return new_employee_code

    def post(self, request):
        status_filter = request.GET.get('status')
        if status_filter:
            if status_filter == 'active':
                employees = Employee.objects.filter(status=True)
            elif status_filter == 'inactive':
                employees = Employee.objects.filter(status=False)
            else:
                employees = Employee.objects.all()
            employee_serializer = EmployeeSerializer(employees, many=True)
            return Response(employee_serializer.data, status=status.HTTP_200_OK)

        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employee added successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request,*args, **kwargs):
        employeeID = kwargs.get('employeeID')
        if employeeID:
            try:
                instance = Employee.objects.get(id=employeeID)
                serializer = EmployeeSerializer(instance)
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)
            except Employee.DoesNotExist:
                return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request,*args, **kwargs):
        employeeID = kwargs.get('employeeID')
        try:
            instance = Employee.objects.get(id=employeeID)
            status_value = request.data.get('status')

            # Update status
            if status_value is not None:
                instance.status = status_value
                instance.save()
                return Response({"message": "Employee status updated successfully."}, status=status.HTTP_200_OK)

            # Handle other updates if necessary
            serializer = EmployeeSerializer(instance, partial=True, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Employee updated successfully."}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Employee.DoesNotExist:
            return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request,*args, **kwargs):
        employeeID = kwargs.get('employeeID')
        if not employeeID:
            return Response({'message': 'Employee ID is required for deletion.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = Employee.objects.get(id=employeeID)
            instance.delete()
            return Response({'message': "Employee deleted successfully"}, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        

@csrf_exempt
def toggle_employee_status(request, employee_id):
    if request.method == "POST":
        try:
            employee = Employee.objects.get(id=employee_id)
            employee.status = not employee.status  # Toggle the status
            employee.save()
            return JsonResponse({'status': employee.status}, status=200)
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)






class AttendanceMenus1APIView(APIView):
    def post(self, request):
        data = request.data
        employee_ids = data.get('employee_ids', [])
        attendance_date = data.get('Attendance_date')
        attendance_status_map = {
            '1': 'Present',
            '2': 'Absent',
            '3': 'Sick Leave',
            '4': 'Casual Leave',
            '5': 'Rollback'
        }

        # Check if attendance already exists for the given date
        for employee_id in employee_ids:
            if AttendanceMenus1.objects.filter(employee__id=employee_id, Attendance_date=attendance_date).exists():
                return Response({
                    "message": f"Attendance for employee '{employee_id}' on '{attendance_date}' already exists."
                }, status=status.HTTP_400_BAD_REQUEST)

        # Create new attendance records
        for employee_id in employee_ids:
            data['employee'] = employee_id  
            data['Attendance_status'] = attendance_status_map.get(data['Attendance_status'], data['Attendance_status'])
            serializer = AttendanceMenusSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Attendance added successfully"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        attendance_id = request.query_params.get('AttendanceID')
        date_filter = request.query_params.get('date')  # Get the date filter from query parameters

        if attendance_id:
            try:
                instance = AttendanceMenus1.objects.get(id=attendance_id)
                serializer = AttendanceMenusSerializer(instance)
                return Response(serializer.data)
            except AttendanceMenus1.DoesNotExist:
                return Response({"message": "Attendance record not found."}, status=status.HTTP_404_NOT_FOUND)

        # Filter attendances based on date if provided
        if date_filter:
            attendances = AttendanceMenus1.objects.filter(Attendance_date=date_filter)
        else:
            attendances = AttendanceMenus1.objects.all()

        serializer = AttendanceMenusSerializer(attendances, many=True)
        return Response(serializer.data)

    def put(self, request):
        update_id = request.query_params.get('hiddenID')

        if not update_id:
            return Response({"message": "Missing Attendance ID for update."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = AttendanceMenus1.objects.get(id=update_id)
        except AttendanceMenus1.DoesNotExist:
            return Response({"message": "Attendance record not found."}, status=status.HTTP_404_NOT_FOUND)

        # Update attendance status if specified
        attendance_status = request.data.get('Attendance_status')
        if attendance_status:
            instance.Attendance_status = attendance_status
            instance.save()
            return Response({'message': 'Attendance status updated successfully'}, status=status.HTTP_200_OK)

        serializer = AttendanceMenusSerializer(instance, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Attendance updated successfully"}, status=status.HTTP_200_OK)

        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        attendance_id = request.query_params.get('AttendanceID')

        if not attendance_id:
            return Response({"message": "Missing Attendance ID for deletion."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = AttendanceMenus1.objects.get(id=attendance_id)
            instance.delete()
            return Response({'message': 'Attendance successfully deleted'}, status=status.HTTP_200_OK)
        except AttendanceMenus1.DoesNotExist:
            return Response({"message": "Attendance record not found."}, status=status.HTTP_404_NOT_FOUND)
        





class HolidayAPIView(APIView):
    def post(self,request):
        data = request.data
        holiday_select = data.get('Holiday_select')
        week_off  = data.get('Week_off_select')
        holiday_name = data.get('Holiday_name')
        holiday_date = data.get('Holiday_date')

        if Holiday.objects.filter(Holiday_name__iexact=holiday_name,Holiday_date__iexact=holiday_date).exists():
            return Response({"message": f"In this holiday '{holiday_name}',in the date '{holiday_date}.'"}, status=status.HTTP_400_BAD_REQUEST)
        elif Holiday.objects.filter(Week_off_select__iexact=holiday_name,Holiday_date__iexact=holiday_date).exists():
            return Response({"message": f"In this Week off '{week_off}',in the date '{holiday_date}.'"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = HolidaySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f" '{holiday_select}' added successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    def get(self,request):
        holidayID = request.query_params.get('holidayID')
        if holidayID:
            instance = Holiday.objects.get(id = holidayID)
            serializer = HolidaySerializer(instance)
        else:
            holidays = Holiday.objects.all()
            serializer = HolidaySerializer(holidays,many = True)
        return Response(serializer.data)    

    def delete(self,request):
        holidayID = request.query_params.get('holidayID')
        instance = Holiday.objects.get(id = holidayID)
        instance.delete()
        return Response({'message': "Holiday is Successfully deleted"},status=status.HTTP_200_OK)

"""

""" 

