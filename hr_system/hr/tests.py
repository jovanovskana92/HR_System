from django.test import TestCase
from .models import Department, Employee, LeaveRequest
from django.urls import reverse


class ModelTestCase(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name='IT', description='IT')
        self.employee = Employee.objects.create(first_name='Tina', last_name='Rafajlovska', email='tina@tina.com',
                                                department=self.department, hire_date='2024-01-01')
        self.leave_request = LeaveRequest.objects.create(employee=self.employee, start_date='2024-02-01',
                                                         end_date='2024-02-03', reason='Vacation')

    def test_department_creation(self):
        self.assertEqual(self.department.name, 'IT')
        self.assertEqual(self.department.description, 'IT')

    def test_employee_creation(self):
        self.assertEqual(self.employee.first_name, 'Tina')
        self.assertEqual(self.employee.last_name, 'Rafajlovska')
        self.assertEqual(self.employee.email, 'tina@tina.com')
        self.assertEqual(self.employee.department, self.department)

    def test_leave_request_creation(self):
        self.assertEqual(self.leave_request.employee, self.employee)
        self.assertEqual(self.leave_request.start_date, '2024-02-01')
        self.assertEqual(self.leave_request.end_date, '2024-02-03')
        self.assertEqual(self.leave_request.reason, 'Vacation')


class ViewTestCase(TestCase):
    def test_department_list_view(self):
        response = self.client.get(reverse('department_list'))
        self.assertEqual(response.status_code, 200)

    def test_employee_list_view(self):
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)

    def test_leave_request_list_view(self):
        response = self.client.get(reverse('leaverequest_list'))
        self.assertEqual(response.status_code, 200)
