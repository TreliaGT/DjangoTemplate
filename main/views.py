from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

# Home page view
def home(request):
    return render(request, "home.html")

# About page view
def about(request):
    return render(request, "about.html")

# Contact page view
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Sending an email
            subject = f"New Contact Form Submission from {contact.name}"
            message = f"Message: {contact.message}\nFrom: {contact.name}\nEmail: {contact.email}"
            recipient_list = ['recipient_email@example.com']  # Change to the email you want to receive notifications
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to the contact page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
