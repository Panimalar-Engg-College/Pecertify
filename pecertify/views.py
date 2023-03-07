from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from random import randint
from db.models import *
from util.func import generate_cert
import csv, io
from io import StringIO, BytesIO

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
            return redirect('index')
        else:
            return redirect('index')
    return redirect('index')

def ulogout(request):
    logout(request)
    return redirect('index')

def generatecert(request):
    if request.method == 'POST':
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
        return redirect('index')
    return redirect('index')

def downloadcert(request):
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