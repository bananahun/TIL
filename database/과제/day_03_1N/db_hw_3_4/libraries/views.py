from django.shortcuts import render, redirect
from .models import Author
from .forms import BookForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    books = author.book_set.all()
    form = BookForm()
    context = {
        'author': author,
        'form' : form,
        'books' : books,
    }
    return render(request, 'libraries/detail.html', context)

def books_create(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    books = author.book_set.all() # 밑에 있는 전체 도서목록을 위한 것
    books_form = BookForm(request.POST)
    # iloveu = len(author.book_set.all())
    if books_form.is_valid():
        # author_id 라는 것을 알려주는 것
        # 마루라는 것을 사용자가 입력 안해도 알려주는 것
        book =books_form.save(commit=False)
        book.author = author
        book.save()
        return redirect('libraries:detail', author_pk)
    context = {
        'author' : author,
        'books_form' : books_form,
        'books' : books,
        # 'iloveu' : iloveu,
    }
    return render(request, 'libraries/detail.html', context)