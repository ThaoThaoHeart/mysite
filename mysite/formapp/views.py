from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'formapp/contact.html', context)

def contact_success_view(request):
    return render(request, 'formapp/contact_success.html')