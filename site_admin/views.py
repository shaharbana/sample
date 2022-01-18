from django.shortcuts import render,redirect
from site_admin.models import*
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def Register(request):
    return render(request,'register.html')
def registerAction(request):
    name=request.POST['name']
    dob=request.POST['dob']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['password']
    user=user_tb(name=name,dob=dob,address=address,username=username,password=password)
    user.save()
    messages.add_message(request,messages.INFO,"Registration successful")
    return redirect('index')
def Login(request):
    return render(request,'login.html')
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    user=user_tb.objects.filter(username=username,password=password)
    admin=admin_tb.objects.filter(username=username,password=password)
    if user.count()>0:
        request.session['id']=user[0].id
        status=user[0].status
        if status == 'approved':
            return render(request,'user/homeuser.html',{'data':user})
        else:
            messages.add_message(request,messages.INFO,"Waiting for approval")
            return redirect('Login')
        
    elif admin.count()>0:
        request.session['id']=admin[0].id
        return render(request,'admin/homeadmin.html',{'data':admin})
    else:
        messages.add_message(request,messages.INFO,"incorrect username or password")
        redirect('Login')

def viewAllUsers(request):
    user=user_tb.objects.all()
    return render(request,'admin/viewAllUsers.html',{'data':user})
def approve(request,uid):
    user_tb.objects.filter(id=uid).update(status='approved')
    return redirect('viewAllUsers')
def reject(request,uid):
    user_tb.objects.filter(id=uid).update(status='rejected')
    return redirect('viewAllUsers')

def delete(request,uid):
     user_tb.objects.filter(id=uid).delete()
    
def EditProfile(request):
    uid=request.session['id']
    user=user_tb.objects.filter(id=uid)
    return render(request,'user/EditProfile.html',{'data':user})
def EditProfileAction(request):
    uid=request.session['id']
    name=request.POST['name']
    dob=request.POST['dob']
    address=request.POST['address']
    username=request.POST['username']
    user=user_tb.objects.filter(id=uid).update(name=name,dob=dob,address=address,username=username)
    messages.add_message(request,messages.INFO,"profile updated")
    return redirect('EditProfile')
def AddReview(request):
    return render(request,'AddReview.html')
def addReviewAction(request):
    rating=request.POST['rating']
    feedback=request.POST['feedback']
    rate=rating_tb(rate=rating,feedback=feedback)
    rate.save()
    messages.add_message(request,messages.INFO,"Rating submitted")
    return redirect('AddReview')
def ViewReview(request):
    rate=rating_tb.objects.all()
    return render(request,'ViewReview.html',{'data':rate})
def html2pdf(request):
    return render(request,'html2pdf.html')

    
