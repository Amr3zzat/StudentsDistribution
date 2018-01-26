from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render ,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import password_reset, password_reset_confirm
from .models import studentForm, UserForm


# Create your views here.


def home(request):
    return render(request,'index.html')





def list(request):
    users = User.objects.all()
    return render(request, "panel.html", {"allusers": users})



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
        return redirect("panel")




