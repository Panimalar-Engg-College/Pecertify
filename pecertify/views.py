from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from random import randint
from db.models import *
from util.func import generate_cert
import csv, io
from io import BytesIO
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def ulogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('index')
    return redirect('index')

def ulogout(request):
    logout(request)
    messages.success(request, 'Logged out Successfully')
    return redirect('index')

def generatecert(request):
    if request.method == 'POST':
        if request.POST['excel_file']=="":
            messages.error(request, 'Please Upload a CSV File')
            return redirect('index')
        excel_file = request.FILES['excel_file']
        file = excel_file.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        data = [line for line in reader]
        
        for i in data:
            cert = Certificate()
            cert.StudentName = i['StudentName']
            cert.StudentEmail = i['StudentEmail']
            cert.StudentCollege = i['StudentCollege']
            cert.CreatedBy = request.user
            cert.save()
            generate_cert(i['StudentName']).save('media/certificates/'+str(cert.id)+'.png')
        messages.success(request, 'Certificates Generated Successfully')
        return redirect('index')
    return redirect('index')

def downloadcert(request):
    if Certificate.objects.filter(CreatedBy=request.user).exists():
        from zipfile import ZipFile
        f = BytesIO()
        zipObj = ZipFile(f, 'w')
        for i in Certificate.objects.filter(CreatedBy=request.user):
            file = 'media/certificates/'+str(i.id)+'.png'
            zipObj.write(file, arcname=f'{i.id}.png')
        zipObj.close()
        response = HttpResponse(f.getvalue(), content_type="application/zip")
        response['Content-Disposition'] = 'attachment; filename=certificates.zip'
        return response
    else:
        messages.error(request, 'No Certificates Found for Download')
        return redirect('index')

def errorhandler(request,exception=None):
    messages.error(request, 'Something Went Wrong, Contact Admin.\n\nSorry for the Inconvenience')
    return redirect('index')