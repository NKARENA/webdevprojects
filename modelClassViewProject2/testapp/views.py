from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class CompanyListView(ListView):
    model = Company
    
class CompanyDetailView(DetailView):
    model = Company
    
class CompanyCreateView(CreateView):
    model = Company
    fields=['name','location','ceo']
    #default template name for create view: <ModelName>_form.html
    #company_form.html
    
class CompanyUpdateView(UpdateView):
    model = Company
    fields=['name','ceo']
    #no need to create any separate template file for update, django uses the template for create view itself
    
class CompanyDeleteView(DeleteView):
    model=Company
    success_url = reverse_lazy('companies')
    #default template for delete view (confirmation template): <ModelName>_confirm_delete.html
    #company_confirm_delete.html
    #default context from delete view: <ModelName>
    #company