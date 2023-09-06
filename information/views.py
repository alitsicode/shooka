from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Why_Choose_Us,FAQ,ContactUs,Company_Work_Together
from accounts.models import Team_Member
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.views import generic
# Create your views here.
def about_us(request):
    companies=Company_Work_Together.objects.all()
    contacts=ContactUs.objects.filter(show_as_client_think=True)
    team_members=Team_Member.objects.all()
    faqs=FAQ.objects.all()
    why_us=Why_Choose_Us.objects.order_by('-created')[:4]
    return render(request,'information/about.html',context={'why_us':why_us,'faqs':faqs,'team_members':team_members,'contacts':contacts,'companies':companies})

class ContactUsCreateView(generic.CreateView):
    model = ContactUs
    template_name = "information/contact.html"
    success_url=reverse_lazy('home')
    fields=['fullname','email','text']
    def form_valid(self, form):
        messages.success(self.request,_("your message successfully send to us"),'success')
        return super().form_valid(form)
