from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q

# Create your views here.
def retrieve_view(request):
    # emp_list = Employee.objects.all()
    # print(type(emp_list))
    # emp_list = Employee.objects.filter(esal__gte=300000)
    # emp_list = Employee.objects.filter(ename__startswith="D") | Employee.objects.filter(esal__lt=300000)
    # emp_list = Employee.objects.filter(Q(ename__startswith="D") | Q(esal__lt=300000))
    # emp_list = Employee.objects.exclude(ename__startswith='J')
    emp_list = Employee.objects.filter(~Q(ename__startswith="J"))
    return render(request, 'testapp/index.html', {'emp_list':emp_list})