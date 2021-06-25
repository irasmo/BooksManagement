from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from rest_framework.generics import get_object_or_404

from books.form import BookForm
from books.models import Book


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return Book.objects.all()


class ContactDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = BookForm()

    return render(request, 'create.html', {'form': form})


def edit(request, pk, template_name='edit.html'):
    contact = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'edit.html', {'form': form})


def delete(request, pk, template_name='confirm_delete.html'):
    contact = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object': contact})