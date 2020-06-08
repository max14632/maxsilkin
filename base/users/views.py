from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            """
            #send_mail(subject,message,from_email,to_list,fail_silently=True)
            subject = 'New User Created'
            message = 'New user have been created succesfully.'
            from_email = settings.EMAIL_HOST_USER
            to_list = ['maxsilkin.com']
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            """

            username = form.cleaned_data.get('username')

            messages.success(request,f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
