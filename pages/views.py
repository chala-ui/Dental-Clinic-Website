from django.shortcuts import render
from django.core.mail import send_mail
import os

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Send Email
        send_mail(
            'Make an Appointment for ' + name, # Subject
            message, # Body
            email, # From Email
            [os.environ.get('User_Email'),], # To Email
        )

        return render(request, 'pages/contact.html', {'name': name})
    
    return render(request, 'pages/contact.html', {})

def about(request):
    return render(request, 'pages/about.html')

def blog(request):
    return render(request, 'pages/blog.html')

def blog_details(request):
    return render(request, 'pages/blog-details.html')

def pricing(request):
    return render(request, 'pages/pricing.html')

def services(request):
    return render(request, 'pages/services.html')

def appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        date = request.POST['date']
        time = request.POST['time']
        message = request.POST['message']

        context = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address,
            'date': date,
            'time': time,
            'message': message
        }

        appointme = "Name: " + name + " Phone: " + phone + " Email: " + email + " Message: " + message + " Date: " + date + " Time: " + time
        # Send Email
        send_mail(
            'Appointment request by' + name, # Subject
            appointment, # Body
            email, # From Email
            [os.environ.get('User_Email'),], # To Email
        )
        
        return render(request, 'pages/appointment.html', context)
    
    return render(request, 'pages/index.html', {})