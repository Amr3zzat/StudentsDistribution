from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import password_reset, password_reset_confirm
from .models import studentForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import student ,updateForm
from django.db import transaction
from .mail import sendmail


# Create your views here.


def home(request):
    return render(request,"index.html")



@login_required
@staff_member_required
def list(request):
    users = User.objects.filter(is_staff=False)
    return render(request, "panel.html", {'allusers': users})


@login_required
@staff_member_required
def add_stu(request):
    if request.method == 'GET':
        return render(request, "add_student.html")
    else:
        user_form = UserForm(request.POST)
        profile_form = studentForm(request.POST)

        new_user = user_form.save(commit=False)
        pas = user_form.cleaned_data['password']
        new_user.set_password(pas)
        new_user.save()
        profile = profile_form.save(commit=False)
        profile.user = new_user
        profile.save()
        return redirect('/panel')


def signin(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)

                if user is not None:
                    if user.is_active:
                        login(request, user)
                        if user.is_staff:
                            return redirect('/panel')
                        else:
                            return redirect('/select')

                    else:
                        messages.add_message(request, messages.ERROR, 'Your account is desactivated.')
                        return render(request, 'login.html')
                else:
                    messages.add_message(request, messages.ERROR, 'Username or password invalid.')
                    return render(request, 'login.html')
            else:
                return render(request, 'login.html')


def signout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        form = updateForm(request.POST, instance=request.user.student)
        if form.is_valid():
            form.save()
            messages.success(request, u'Your profile were successfully edited.')
            user = request.user
            m = "Your depart is " + user.student.get_Department_display()
            n = str(m)
            sendmail(user.email, n)
            return redirect(('/select'))

    else:
        form = updateForm(instance=request.user.student)
        user = request.user

    return render(request, 'select.html', {'form': form,'username':user})
