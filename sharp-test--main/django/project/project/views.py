from django . http import HttpResponse
from django . shortcuts import render
from project import views
from app.models import Exam
from app.models import Gk
from app.models import Django
from app.models import Register
from django.contrib import messages
from app .models import Answer

from django.shortcuts import render, redirect



# Create your views here.
def webpage1(request):
    return render(request,'index.html')

def webpage2(request):
    return render(request,'login.html')

def webpage3(request):
    return render(request,'all-quiz.html')

def webpage4(request):
       django=Django.objects.all()
       return render(request,"computer.html",{"django":django})


def webpage5(request):
    return render(request,'leaderboard.html')


def webpage6(request):
       gk=Gk.objects.all()
       return render(request,"gk.html",{"gk":gk})


def webpage7(request):
    return render(request,'life.html')


def webpage8(request):
    return render(request,'math.html')


def webpage9(request):
    return render(request,'physics.html')

def webpage10(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        saverecord = Register(email=email, username=username, password=password)
        saverecord.save()
        messages.success(request, 'Record saved successfully!')
        return HttpResponse("This is a POST request")
    else:
        return render(request, 'register.html')

def webpage11(request):
    return render(request,'blogs.html')

def webpage12(request):
    return render(request,'confirm.html')

def webpage13(request):
    return render(request,'contact-us.html')

def webpage14(request):
    return render(request,'dashboard.html')

def webpage15(request):
    return render(request,'downloads.html')

def webpage16(request):
    return render(request,'message.html')

def webpage17(request):
    return render(request,'profile-edit.html')

def webpage18(request):
    return render(request,'terms and condition.html')


def webpage19(request):
    return render(request,'profile.html')


def home(request):
    exam=Exam.objects.all()
    return render(request,"question.html",{"exam":exam})
def show(request):
    userdetails = Answer.objects.all()
    return render(request, "admin/userinfo.html", {'userdetails': userdetails})


#def quiz_result(request, quiz_id, score):
 #   return render(request, 'quiz_app/quiz_result.html', {'quiz_id': quiz_id, 'score': score})
