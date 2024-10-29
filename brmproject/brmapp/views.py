
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, "viewbook.html", {"books": books})

def addBookView(request):
    return render(request, "addbook.html")

def addBook(request):
    if request.method == "POST":
        t = request.POST["title"]
        p = request.POST["price"]
        book = Book(title=t, price=p)
        book.save()
        return redirect('home')

def editBookView(request):
    book_id = request.GET.get('bookid')
    book = Book.objects.get(id=book_id)
    return render(request, "editbook.html", {"book": book})

def editBook(request):
    if request.method == "POST":
        t = request.POST["title"]
        p = request.POST["price"]
        book = Book.objects.get(id=request.POST['bid'])
        book.title = t
        book.price = p
        book.save()
        return redirect('home')

def deleteBookView(request):
    book_id = request.GET.get('bookid') 
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('home')
