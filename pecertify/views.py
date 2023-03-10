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
        try:
            if request.POST['excel_file']=="":
                messages.error(request, 'Please Upload a CSV File')
                return redirect('index')
        except:
            excel_file = request.FILES['excel_file']
            file = excel_file.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(file))
            data = [line for line in reader]
            dept=request.user.department.department
            try:
                for i in data:
                    try:
                        cert = Certificate()
                        cert.Name = i['Name']
                        cert.College = i['College']
                        cert.Event = i['Event']
                        cert.ID = i['ID']
                        cert.CreatedBy = request.user
                        cert.save()
                    except:
                        messages.error(request, 'Error Saving Certificates to Database')
                        return redirect('index')
                    print()
                    try:
                        generate_cert(i['Name'],i['College'],i['Event'],dept).save('media/certificates/'+str(cert.id)+'.png')
                    except:
                        messages.error(request, 'Error Generating Certificates')
                        return redirect('index')
                messages.success(request, 'Certificates Generated Successfully')
                return redirect('index')
            except:
                messages.error(request, 'Please Upload a Valid CSV File with Correct Column Names.')
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
    print(exception)
    messages.error(request, 'Something Went Wrong, Contact Admin.\n\nSorry for the Inconvenience')
    return redirect('index')