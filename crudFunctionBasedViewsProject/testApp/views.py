from django.shortcuts import render, redirect
from testApp.models import Employee
from testApp.forms import EmployeeForm

# Create your views here.


def retrieve_view(request):
    employees = Employee.objects.all()
    return render(request, 'testAppTem/index.html', {'employees': employees})


def create_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request, 'testAppTem/create.html', {'form': form})


def update_view(request, id):
    employee = Employee.objects.get(id=id)
    # test = Employee.objects.get(id=15)
    # print(test.eaddr)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    return render(request, 'testAppTem/update.html', {'employee': employee})

def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/")


            