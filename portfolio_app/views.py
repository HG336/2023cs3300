from django.shortcuts import render
from django.http import HttpResponse 
from django.views import generic
from .models import Student

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
