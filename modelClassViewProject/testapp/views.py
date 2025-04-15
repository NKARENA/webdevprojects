from django.shortcuts import render
from django.views.generic import ListView, DetailView   
from testapp.models import Book

# Create your views here.
class BookListView(ListView):
    model=Book
    # default template of list view: <ModelName>_list.html
    # book_list.html 
    # default context object of list view: <ModelName>_list
    # book_list
    
class BookDetailView(DetailView):
    model=Book
    # default template of detail view: <ModelName>_detail.html
    # book_detail.html 
    # default context object of list view: <ModelName> or object
    # book (or) object