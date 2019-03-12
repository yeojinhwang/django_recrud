import pprint
from django.shortcuts import render, HttpResponse, redirect
from .models import Board

# Create your views here.

def index(request):
    # pprint.pprint(request)
    # pprint.pprint(type(request))
    # pprint.pprint(dir(request))
    # print(request.scheme)
    # print(request.get_host())
    # print(request.get_full_path())
    # print(request.build_absolute_uri())
    # print(request.method)
    # pprint.pprint(request.META)
    contents = Board.objects.order_by('-id')
    return render(request, 'boards/index.html', {'contents': contents})
    
def new(request):
    if request.method == 'POST':
        board = Board()
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:index')
    else:
        return render(request, 'boards/new.html')
    
# def create(request):
#     board = Board()
#     board.title = request.POST.get('title')
#     board.content = request.POST.get('content')
#     board.save()
#     return redirect('boards:index')
    
def edit(request, pk):
    if request.method == 'POST':
        board = Board.objects.get(pk=pk)
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:index')
    else:
        board = Board.objects.get(pk=pk)
        return render(request, 'boards/edit.html', {'board': board})
    
# def update(request, pk):
#     board = Board.objects.get(pk=pk)
#     board.title = request.POST.get('title')
#     board.content = request.POST.get('content')
#     board.save()
#     return redirect('boards:index')

def delete(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:index')