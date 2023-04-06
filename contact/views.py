from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import CreateView,View
from .models import ContactLink

class ContactView(View):
    def get(self,request):
        contacts = ContactLink.objects.all()
        form = ContactForm
        return render(request,'contact/contact.html',{'contacts': contacts, 'form': form})


class CreateContact(CreateView):
    form_class = ContactForm
    success_url = '/'