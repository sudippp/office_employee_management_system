from django.shortcuts import render, HttpResponse
from .forms import*
from django.contrib import messages
# Create your views here.
def base(request):
    return render (request,'base.html')

def home(request):
    return render (request,'home.html')

def manager_register(request):
    user = SignupForm()
    if request.method == "POST":
        user = SignupForm(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'Your Profile Created Successfully !!')

    context = {'user': user}
    return render(request, 'manager_registration.html', context)

def add_emp(request):
    empfrom = EmployeeForm()
    context = {'empfrom':empfrom}
    if request.method == "POST":
        empfrom = EmployeeForm(request.POST)
        if empfrom.is_valid():
            empfrom.save()
            messages.success(request, 'Employee Created Successfully !!')
    return render(request,'add_emp.html',context)

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'all_emp.html', context)

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Deleted !!")
        except:
            return HttpResponse("Try Another ID !!")
    epms = Employee.objects.all()
    context = {
        'epms':epms
    }
    return render(request, 'remove_emp.html',context)


def filter_emp(request):
    if request.method == "POST":
        id = request.POST['ID']

        emp_id = Employee.objects.filter(employee_id=id)
        print(id)
        return render(request, 'filter_emp.html', {'emp_id': emp_id})

    elif request.method == "GET":
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("Please Enter valid Employee ID !!")


def update_emp(request):
    if request.method == "POST":
        id = request.POST['ID']
        emp_id = Employee.objects.filter(employee_id=id)
        print(id)
        if request.POST['first_name']:
            new_first_name = request.POST['first_name']
            update_name = Employee.objects.filter(employee_id=id).update(first_name=new_first_name)
            messages.success(request, 'Employee Updated Successfully !!')
            return render(request, 'update_emp.html')
        elif request.POST['last_name']:
            new_last_name = request.POST['last_name']
            update_name = Employee.objects.filter(employee_id=id).update(last_name=new_last_name)
            messages.success(request, 'Employee Updated Successfully !!')
            return render(request, 'update_emp.html')
        elif request.POST['department']:
            new_department = request.POST['department']
            update_name = Employee.objects.filter(employee_id=id).update(department=new_department)
            messages.success(request, 'Employee Updated Successfully !!')
            return render(request, 'update_emp.html')
        elif request.POST['role']:
            new_role = request.POST['role']
            update_name = Employee.objects.filter(employee_id=id).update(role=new_role)
            messages.success(request, 'Employee Updated Successfully !!')
            return render(request, 'update_emp.html')
        elif request.POST['salary']:
            new_salary = request.POST['salary']
            update_name = Employee.objects.filter(employee_id=id).update(salary=new_salary)
            messages.success(request, 'Employee Updated Successfully !!')
            return render(request, 'update_emp.html')
        elif request.POST['bonus']:
            new_bonus = request.POST['bonus']
            update_name = Employee.objects.filter(employee_id=id).update(bonus=new_bonus)
            messages.success(request, 'Employee Updated Successfully !!')
            return render(request, 'update_emp.html')
        elif request.POST['email']:
            new_email = request.POST['email']
            update_name = Employee.objects.filter(employee_id=id).update(email_id=new_email)
            messages.success(request, 'Employee Updated Successfully !!')
            return render(request, 'update_emp.html')
        elif request.POST['phone_number']:
            new_phone_number = request.POST['phone_number']
            update_name = Employee.objects.filter(employee_id=id).update(phone_number=new_phone_number)
            messages.success(request, 'Employee Updated Successfully !!')
            return render(request, 'update_emp.html')

        else:
            return render(request, 'update_emp.html', {'emp_id': emp_id})

    elif request.method == "GET":
        return render(request, 'update_emp.html')
    else:
        return HttpResponse("Please Enter valid Employee ID !!")