from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    comments = book.review_set.all()
    comment_form = CommentForm()
    context = {
        'book': book,
        'comment_form': comment_form,
        'comments':comments,
    }
    return render(request, 'libraries/detail.html', context)


def comments_create(request, pk):
    book = Book.objects.get(pk=pk)
    comments = book.review_set.all()
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.book = book
        comment.user = request.user
        comment.save()
        return redirect('libraries:detail', book.pk)
    context = {
        'comment_form': comment_form,
        'book': book,
        'comments': comments,
    }
    return render(request, 'libraries/detail.html', context)

def comments_delete(request,comment_pk, book_pk):
    comment = Review.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('libraries:detail', book_pk)