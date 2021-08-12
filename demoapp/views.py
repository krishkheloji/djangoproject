from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Books, Contact, Student
from .forms import BooksForm, StudentForm
from django.conf import settings 
from django.core.files.storage import FileSystemStorage
from django.core.mail import message, send_mail
import csv
from reportlab.pdfgen import canvas
# Create your views here.

def home(request):
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        url=fs.url(myfile)
        print('Save')
    #dict={'name':'Pride','id':101}
    return render(request,'index.html')

def test(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print('Save')
    else:
        form=StudentForm()            
    return render(request,'test.html',{'form':form})


def contact(request):
    if request.method== "POST":    
        uname=request.POST['ename']
        uemail=request.POST['Email']

        con=Contact(name=uname,email=uemail)
        con.save()

        print('Save Success')

    records=Contact.objects.all()
    d={'records':records}
    return render(request,'contact.html',d)

def add(request):
    a=int(request.POST['num1'])
    b=int(request.POST['num2'])

    c=a+b

    return render(request,'result.html',{'sum':c})

def upload_book(request):
    if request.method=='POST':
      form=BooksForm(request.POST,request.FILES)
      if form.is_valid:
          form.save()  
          print('Save')
          return redirect('book_list')
    else:
        form=BooksForm()
    return render(request,'upload_book.html',{'book':form})


def book_list(request):
    b=Books.objects.all()
    return render(request,'book_list.html',{'books':b})


def delete_book(request,pk):
    if request.method=='POST':
        book=Books.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

def send_email(request):
    if request.method=='POST':
        message=request.POST['message']
        to=request.POST['to']
        send_mail('Testing',
            message,settings.EMAIL_HOST_USER,[to],fail_silently=False)

    return render(request,'send_email.html')


def ssession(request):
    request.session['ename']='Pride'
    request.session['email']='pride@gmail.com'
    return HttpResponse("Session are set")

def gsession(request):
    name=request.session['ename']
    email=request.session['email']
    return HttpResponse(email)


def scookie(request):
    response=HttpResponse("Cookie are set")
    response.set_cookie('user','Pride')
    return response

def gcookie(request):
    name=request.COOKIES['user']
    return HttpResponse(name)

def csvs(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="file.csv"'
    st=Student.objects.all()
    writer=csv.writer(response)
    for s in st:
        writer.writerow([s.name,s.email,s.mobile])
    return response

def getpdf(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment; filename="file.pdf"'
    p=canvas.Canvas(response)
    p.setFont("Times-Roman",55)
    p.drawString(100,700,"Welcome to DJango.")
    p.showpage()
    p.save()
    return response














