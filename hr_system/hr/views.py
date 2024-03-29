from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .models import Department, Employee, LeaveRequest
from .serializers import DepartmentSerializer, EmployeeSerializer, LeaveRequestSerializer
from .forms import DepartmentForm, EmployeeForm, LeaveRequestForm


# Django views for rendering templates
def homepage(request):
    return render(request, 'hr/home.html')


def department_list(request):
    departments = Department.objects.all()
    return render(request, 'hr/department_list.html', {'departments': departments})


def employee_list(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()  # Retrieve departments queryset
    # Filter employees by department if a department is selected
    department_id = request.GET.get('department')
    if department_id:
        employees = employees.filter(department_id=department_id)
    return render(request, 'hr/employee_list.html', {'employees': employees, 'departments': departments})


def leaverequest_list(request):
    leave_requests = LeaveRequest.objects.all().order_by('start_date')
    return render(request, 'hr/leaverequest_list.html', {'leave_requests': leave_requests})


def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    employees = Employee.objects.filter(department=department)
    return render(request, 'hr/department_detail.html', {'department': department, 'employees': employees})


def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'hr/employee_detail.html', {'employee': employee})


def leaverequest_detail(request, pk):
    leaverequest = get_object_or_404(LeaveRequest, pk=pk)
    return render(request, 'hr/leaverequest_detail.html', {'leaverequest': leaverequest})


# Form views for rendering templates
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'hr/department_create.html', {'form': form})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'hr/employee_create.html', {'form': form})


def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'hr/employee_delete_confirm.html', {'employee': employee})


def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'hr/employee_update_form.html', {'form': form, 'employee': employee})


def leaverequest_create(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leaverequest_list')
    else:
        form = LeaveRequestForm()
    return render(request, 'hr/leaverequest_create.html', {'form': form})


# DRF views for APIs
class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class LeaveRequestListCreateAPIView(generics.ListCreateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer


class LeaveRequestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
