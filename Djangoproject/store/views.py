from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from store.models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'store/index.html')

def bookDetailView(request, bid):
    obj= get_object_or_404(Book,id=bid)
    template_name='store/book_detail.html'
    context={
        'book':obj, # set this to an instance of the required book
        'num_available':None # set this 1 if any copy of this book is available, otherwise 0
    }
    # START YOUR CODE HERE

    try:
        BookCopy.objects.get(book=Book.objects.get(id=bid))
        context={
        'book':obj,
        'num_available': 0
        }
    except:
        context={
        'book':obj,
        'num_available': 1
        }
    return render(request,template_name, context=context)


def bookListView(request):

    template_name='store/book_list.html'
    context={
        'books':None, # set here the list of required books upon filtering using the GET parameters
    }

    get_data = request.GET
    # START YOUR CODE HERE
    queries = ['title', 'author', 'genre']
    for x in queries:
        query = get_data.get(x,None)
        books=Book.objects.all()

        if query is not None:
            books = books.filter(
                            Q(title__icontains=query) |
                            Q(author__icontains=query) |
                            Q(genre__icontains=query)
                            )
            break
    context={
        'books':books,
        }


    return render(request,template_name, context=context)

@login_required
def viewLoanedBooks(request):
    template_name='store/loaned_books.html'
    context={
        'books':None,
    }
    '''
    The above key books in dictionary context should contain a list of instances of the
    bookcopy model. Only those books should be included which have been loaned by the user.
    '''
    # START YOUR CODE HERE
    context={

    'books':BookCopy.objects.filter(borrower=request.user)
    }

    return render(request,template_name,context=context)

@csrf_exempt
@login_required
def loanBookView(request):
    response_data={
        'message':None,
    }
    '''
    Check if an instance of the asked book is available.
    If yes, then set message to 'success', otherwise 'failure'
    '''
    # START YOUR CODE HERE
    book_id = request.POST['bid'] # get the book id from post data

    try:
        BookCopy.objects.get(book=Book.objects.get(id=book_id))
        response_data={
        'message': 0,
        }
    except:
        BookCopy.objects.create(book=Book.objects.get(id=book_id), borrower=request.user, borrow_date=datetime.now())
        response_data={
        'message': 1,
        }

    return JsonResponse(response_data)

'''
FILL IN THE BELOW VIEW BY YOURSELF.
This view will return the issued book.
You need to accept the book id as argument from a post request.
You additionally need to complete the returnBook function in the loaned_books.html file
to make this feature complete
'''
@csrf_exempt
@login_required
def returnBookView(request):
    data={
        'message':None,
    }

    # START YOUR CODE HERE
    book_id=request.POST['bid'] # get the book id from post data
    try:
        BookCopy.objects.get(book=Book.objects.get(id=book_id)).delete()
        response_data={
            'message': 1,
            }

    except:
        #BookCopy.objects.get(book=Book.objects.get(bid=book_id))
        response_data={
            'message': 0,
            }

    return JsonResponse(response_data)
