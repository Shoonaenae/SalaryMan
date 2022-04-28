from django.core.checks import messages
from django.forms.widgets import EmailInput
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import *
from django.contrib import messages
from django.http import JsonResponse, request
from django.contrib.auth.models import User, auth
from .models import *

# Create your views here.
class HomeView(View):
    def get(self, request):         
        return render(request,'home.html')

class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return render(request,'home.html')

class FeatureView(View):
    def get(self, request):     
        return render(request,'feature.html')

class DashboardView(View):
    def get(self, request): 
        employers = Employer.objects.all()
        employees = Employee.objects.all()
        city = City.objects.all()
        salaries = Salary.objects.all()
    

        """
        > pass the view to template
        > may contain 1/more vars
        """
        context = {
            'employer': employers,
            'employee': employees,
            'city': city,
            'salary': salaries
           
        }
        return render(request,'dashboard.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdateEmployer' in request.POST:
                print('Update button clicked')
                employer_id = request.POST.get("employer_id")
                fname = request.POST.get("firstname")
                lname = request.POST.get("lastname")
                city = request.POST.get("city")

                updateEmployer = Employer.objects.filter(employer_id = employer_id).update(firstname = fname, lastname = lname, city_id_id = city)
                print(updateEmployer)
                print("PROFILE UPDATED")

            if 'btnDeleteEmployer' in request.POST:
                employerID = request.POST.get("employer_id")
                employer = Employer.objects.filter(employer_id = employerID).delete()

            if 'btnUpdateEmployee' in request.POST:
                print('Update button clicked')
                employee_id = request.POST.get("employee_id")
                fname = request.POST.get("firstname")
                lname = request.POST.get("lastname")
                age = request.POST.get("age")
                cnumber = request.POST.get("contact")
                city = request.POST.get("city")
                year_hired = request.POST.get("year_hired")
                employer_id = request.POST.get("employerid")

                update_employee = Employee.objects.filter(employee_id = employee_id).update(firstname = fname, lastname = lname, age = age, contact_num = cnumber, city_id_id = city)
                print(update_employee)
                print('PROFILE UPDATED')
            if 'btnDeleteEmployee' in request.POST:
                print('DELETE BUTTON IS CLICKED')
                employee_id = request.POST.get("employee_id")
                e = Employee.objects.filter(employee_id = employee_id).delete()
                print("DELETED")

            if 'btnUpdateSalary' in request.POST:
                print('Update button clicked')
                salary_id = request.POST.get("salary_id")
                employeeid = request.POST.get("lastname")
                amount = request.POST.get("amount")
        
                updateSalary = Salary.objects.filter(salary_id = salary_id).update(amount = amount)
                print(updateSalary)
                print("PROFILE UPDATED")
     
            elif 'btnDeleteSalary' in request.POST:
                print('DELETE BUTTON IS CLICKED')
                salary_id = request.POST.get("salary_id")
                salary = Salary.objects.filter(salary_id = salary_id).delete()
                print("DELETED")

        return redirect('salarymanagement:dashboard_view')  
class AboutUsView(View):
    def get(self, request):                 
        return render(request,'aboutus.html')

class SignInView(View):
    def get(self, request):                 
        return render(request,'signin.html')
    
    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('salarymanagement:home_view')
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('salarymanagement:sign_in_view')

class SignUpView(View):
    def get(self, request):                 
        return render(request,'signup.html')

    def post(self, request):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username is already taken')
                    return redirect('salarymanagement:sign_up_view')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email is already in use')
                    return redirect('salarymanagement:sign_up_view')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                    user.save()
                    messages.info(request, 'Congratulations, you have successfully registered')
                    return redirect('salarymanagement:sign_in_view')
            else:
                messages.info(request, 'Password does not match')
                return redirect('salarymanagement:sign_up_view')
        
        return redirect('salarymanagement:dashboard_view')

class ContactUsView(View):
    def get(self, request):                 
        return render(request,'contactus.html')

class AddEmployerView(View):
    def get(self, request):
        return render(request, 'addemployer.html', {'city' : City.objects.all()})

    def post(self, request):
        form = EmployerForm(request.POST)
    
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        city_id = request.POST.get("city")

        form = Employer(firstname = fname, lastname = lname, city_id_id = city_id)
        form.save()

        return redirect('salarymanagement:dashboard_view')
    
        #   return HttpResponse('not valid')


class AddEmployeeView(View):
    def get(self, request):
        return render(request, 'addemployee.html', {'employers' : Employer.objects.all(), 'city' : City.objects.all()})

    def post(self, request):
        form = EmployeeForm(request.POST)

        employer_id = request.POST.get("employerid")
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        age = request.POST.get("age")
        cnumber = request.POST.get("contact")
        city = request.POST.get("city")
        form = Employee(employer_id_id = employer_id, firstname = fname, lastname = lname, age = age, contact_num = cnumber, city_id_id = city)
        form.save()

        return redirect('salarymanagement:dashboard_view')

class AddSalaryView(View):
    def get(self, request):                 
        return render(request,'addsalary.html', {'employees' : Employee.objects.all()})

    def post(self, request):
        form = EmployeeForm(request.POST)

        salary_id = request.POST.get("salary_id")
        employee_id = request.POST.get("employee_id")
        amount = request.POST.get("amount")
        
        form = Salary(salary_id = salary_id, employee_id_id = employee_id, amount = amount)
        form.save()

        return redirect('salarymanagement:dashboard_view')