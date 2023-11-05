from django.shortcuts import render
from django.http import HttpResponse 
from django.views import generic
from .models import Student
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Portfolio, Project
from .forms import PortfolioForm


# Create your views here. 

def index(request): 

 
# Render the HTML template index.html with the data in the context variable. 

   return render( request, 'portfolio_app/index.html') 

class StudentListView(generic.ListView): 

   model = Student 

class StudentDetailView(generic.DetailView): 

   model = Student 
def index(request): 

   student_active_portfolios = Student.objects.select_related('Portfolio').all().filter(Portfolio__is_active=True) 

   print("active portfolio query set", student_active_portfolios) 

   return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios}) 
class PortfolioCreate(CreateView):
    model = Portfolio
    
    fields = ['title', 'contact_email', 'is_active']
    template_name = 'portfolio_app/portfolio_form.html'


class PortfolioUpdate(UpdateView):
    model = Portfolio
    fields = ['title', 'contact_email', 'is_active']

class PortfolioDelete(DeleteView):
    model = Portfolio
    success_url = reverse_lazy('portfolio-list')

class PortfolioListView(generic.ListView):
    model = Portfolio

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list') 

class StudentCreate(CreateView):
    model = Student
    fields = ['name', 'major', 'email']  
    success_url = reverse_lazy('student_list')



