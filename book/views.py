from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib import messages
# Create your views here.


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully !!')
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})


def home(request):
    li = Book.objects.all()
    return render(request, 'book/home.html', {'li': li})


def book_detail(request, pk):
    bk = Book.objects.get(pk=pk)
    return render(request, 'book/book_detail.html', {'bk': bk})


def book_update(request, pk):
    bk = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=bk)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully !!')
            return redirect('home')
    else:
        form = BookForm(instance=bk)
    return render(request, 'book/book_form.html', {'form': form})


def book_delete(request, pk):
    bk = Book.objects.get(pk=pk)
    if request.method == 'POST':
        bk.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('home')
    return render(request, 'book/confirm_delete.html', {'bk': bk})
