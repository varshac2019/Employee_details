from django.shortcuts import render,get_object_or_404,redirect
from . models import Employee
from .forms import GetForm

# Create your views here.

def employee_list(request):
    employees = Employee.objects.all()
    return render(request , 'employee/employee_list.html' , {'employees':employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee/employee_detail.html', {'employee': employee})

def employee_new(request):
    if request.method == "GET":
        form = GetForm(request.GET)
        if form.is_valid():
            employee = form.save()
            employee.save()
            return redirect('employee_detail', pk=employee.pk)
    else:
        form = GetForm()
    return render(request, 'employee/employee_edit.html', {'form': form})

