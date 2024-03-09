from django.shortcuts import render,HttpResponseRedirect
from . forms import StudentRegistration
from .models import Student

# Create your views here.
def index(request):
    form=StudentRegistration
    if request.method=='POST':
        form=StudentRegistration(request.POST)
        if form.is_valid():
            form.save(commit=True)
        form=StudentRegistration
    
    data=Student.objects.all()
    return render(request,'index.html',{'form':form,'data':data})


def delete(request):
    id_number=request.GET['id_number']
    obj=Student(id=id_number)
    obj.delete()
    return render(request,'delete.html')

def edit(request):
    id_number=request.GET['id_number']
    name=request.GET['name']
    email=request.GET['email']
    password=request.GET['password']
    update=Student(id=id_number, name=name,email=email,password=password)
    update.save()
    return render(request,'edit.html')