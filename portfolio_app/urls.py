from django.urls import path 

from . import views 
from django.urls import path
from . import views
from .views import PortfolioCreate, PortfolioUpdate, PortfolioDelete
from .views import StudentListView, PortfolioDelete, StudentCreate

 

urlpatterns = [ 

#path function defines a url pattern 

#'' is empty to represent based path to app 

# views.index is the function defined in views.py 

# name='index' parameter is to dynamically create url 

# example in html <a href="{% url 'index' %}">Home</a>. 

    path('', views.index, name='index'), 
    path('students/', StudentListView.as_view(), name='student-list'),
    # Inside your urls.py
    path('portfolios/', views.PortfolioListView.as_view(), name='portfolio-list'),

    path('portfolio/add/', PortfolioCreate.as_view(), name='portfolio-add'),
    path('portfolio/<int:pk>/', PortfolioUpdate.as_view(), name='portfolio-update'),
    path('portfolio/<int:pk>/delete/', PortfolioDelete.as_view(), name='portfolio-delete'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/add/', StudentCreate.as_view(), name='student_add'),
    path('student/<int:pk>/delete/', views.StudentDelete.as_view(), name='student-delete'),

]