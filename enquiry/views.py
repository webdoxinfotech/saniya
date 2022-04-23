from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            return redirect('home')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'enquiry/contact.html', context)