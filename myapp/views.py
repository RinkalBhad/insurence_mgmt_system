from django.shortcuts import render,redirect
from .models import*
from .forms import*
from django.contrib.auth import logout
from django.core.mail import send_mail
from insurence_management_system import settings
# Create your views here.
msg=""
def index(request):
    return render(request,'index.html')

def customerclick(request):
    return render(request,'customerclick.html')

def customersignup(request):
    global msg
    if request.method=="POST":
        data=usersignupform(request.POST,request.FILES)
        if data.is_valid():
            username=data.cleaned_data.get("username")
            try:
                usesignup.objects.get(username=username)
                msg="username already exists"
                return redirect('customersignup')
            except usesignup.DoesNotExist:
                data.save()
                msg="singup successfully"
                return redirect("login")
        else:
            print(data.errors)

    return render(request,'customersignup.html',{"msg":msg})

def aboutus(request):
   
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')

def customerlogin(request):
    global msg
    if request.method=="POST":
        unm=request.POST['username']
        pwd=request.POST['password']

        data=usesignup.objects.filter(username=unm,password=pwd)
        fnm=usesignup.objects.get(username=unm)
        if data:
            msg="login successfully"
            request.session['user']=unm
            return redirect("customer_dashboard")
        else:
            msg="invalid username or password"
    return render(request,'customerlogin.html',{"msg":msg})

def customer_dashboard(request):
    data=Policy.objects.all().count()
    cdata=Policy.objects.all().count()
    kk=Category.objects.all().count()
    ques=questiondata.objects.all().count()
    return render(request,'customer_dashboard.html',{"data":data,"cdata":cdata,"kk":kk,'ques':ques})

def question_history(request):
    data=questiondata.objects.all()
    return render(request,'question_history.html',{'data':data})


def ask_question(request):
    if request.method=="POST":
        ques=Questionform(request.POST)
        if ques.is_valid():
            ques.save()
            print("saved")
            return redirect("quesion_history")
        else:
            print(ques.errors)

    return render(request,'ask_question.html')

def history(request,id):
    user=Policy.objects.get(id=id)
    data=Policy.objects.all()
    return render(request,'history.html',{'user':user,"data":data})

def apply_policy(request):
    data=Policy.objects.all()
    return render(request,'apply_policy.html',{'data':data})

def userlogout(request):
    logout(request)
    return render(request,'userlogout.html')

def customerbase(request):
    user=request.session.get("user")
    return render(request,'customerbase.html',{'user':user})

def another(request):
    user=request.session.get('user')
    if request.method=='POST':
        email=request.POST['email']
        sub='forget password,'
        msg='this is conformaion email for your sefty '
        frm=settings.EMAIL_HOST_USER
        re=[request.POST['email']]
        send_mail(subject=sub,message=msg,from_email=frm,recipient_list=re)
        print("successfull send")
        return redirect('forget')
    return render(request,'another.html',{'user':user})

def forget(request):
    if request.method=="POST":
        pwd=request.POST['password']
        pwd2=request.POST['password2']

        if pwd==pwd2:
            usesignup.objects.update(password=pwd)
            return redirect("/")
    return  render(request,'forget.html')