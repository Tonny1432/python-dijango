from django.shortcuts import render
from . models import students,subject

def student_details(request):
    student_data = students.objects.all()
    return render(request,'data.html',{'std':student_data})
# Create your views here.
def subject_details(request):
    subject_data =subject.objects.all()
    return render(request,'subject.html',{'sub': subject_data})