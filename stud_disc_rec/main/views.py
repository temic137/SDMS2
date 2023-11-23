from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Student,Incidents,Disciplinary_Actions,Notifications,Records,Evidence
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.template import loader
from django.contrib.auth.models import User
from .forms import AdminCheckForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    
    return render(request, 'home.html')
  
    
def staff(request):
    students=Student.objects.all()
    incidents=Incidents.objects.all()
    record=Records.objects.all()
    return render(request,'staff.html',{'students':students,'incidents':incidents,'record':record})

def student(request,pk):
    students = get_object_or_404(Student, pk=pk)

    # Assuming there's a common field like Stud_ID in the related models
    incidents = Incidents.objects.filter(Stud_ID=pk)
    discipline = Disciplinary_Actions.objects.filter(Stud_ID=pk)
    record = Records.objects.filter(Stud_ID=pk)
    evidence = Evidence.objects.filter(Stud_ID=pk)

    return render(request,'student.html',{'students':students,'incidents':incidents, 'discipline':discipline,'record':record,'evidence':evidence})

def search_student(request):
    if request.method=='POST':
        searched=request.POST['searched']
        students=Student.objects.filter(FName__contains=searched)
        return render(request,'search_student.html',{'searched':searched,'students':students})
    else:
        return render(request,'search_student.html',{})

# views.py

def student_login(request):
    if request.method == 'POST':
        stud_id = request.POST.get('stud_id')
        password = request.POST.get('password')

        try:
            students = Student.objects.get(Stud_ID=stud_id)
            
            if students.check_password(password):
                # Authentication successful
                # Redirect to the student page or display information
                incidents = Incidents.objects.filter(Stud_ID=students)
                discipline = Disciplinary_Actions.objects.filter(Stud_ID=students)
                record = Records.objects.filter(Stud_ID=students)
                evidence = Evidence.objects.filter(Stud_ID=students)
                return render(request, 'student.html', {'students': students ,'incidents':incidents,'discipline':discipline,'record':record,'evidence':evidence})
            else:
                messages.error(request, 'Invalid credentials')
        except Student.DoesNotExist:
            messages.error(request, 'Student not found')

    return render(request, 'login.html')


def admin_check(request):
    if request.method == 'POST':
        form = AdminCheckForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_staff:
                login(request, user)
                return redirect('staff')
    else:
        form = AdminCheckForm()

    return render(request, 'login_admin.html', {'form': form})