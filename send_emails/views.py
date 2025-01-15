from django.shortcuts import render ,redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from auto_email_sender import settings
from django.contrib import messages


# ========= home =========
def home (request):
    return render(request , 'home.html')

# send_emails
def send_emails(request):
    return render(request, 'send_emails/send_emails.html')

#=======contact us ========
def contact_us(request):
    if request.method == 'POST':
        subject = "contact_us"
        message = request.POST.get("message", "")
        if subject and message:
            try:
                with open('email_host_user.txt', 'w') as file:
                    file.write(request.POST.get('email',''))
                send_mail(subject, message, settings.EMAIL_HOST_USER, ["aymenzitouni110@gmail.com"])
            except :
                    messages.error(request , 'Soemthing went wrong. Please make sure that you followed the steps.')
            messages.success(request , 'Contact us message has been successfully sent . Thank You 🩷')
        else:
            messages.error(request , 'Soemthing went wrong. Try again!')
        return redirect("home")
