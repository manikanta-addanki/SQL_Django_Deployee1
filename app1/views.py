from django.shortcuts import render,redirect

from app1.models import student
from app1.forms import student_form

def details(request):
    data = student.objects.all()
    context = {
        'data':data
    }
    return render(request,'home.html',context)

def new_student(request):
    form = student_form()
    if request.method == 'POST':
        form = student_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home101')
    else:
        form = student_form()
        context = {
            'form':form
        }
    return render(request,'std_form.html',context)
