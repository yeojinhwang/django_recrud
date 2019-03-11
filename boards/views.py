from django.shortcuts import render, HttpResponse, redirect
from .models import Board

# Create your views here.

def index(request):
    contents = Board.objects.order_by('-id')
    return render(request, 'boards/index.html', {'contents': contents})
    
def new(request):
    return render(request, 'boards/new.html')
    
def create(request):
    board = Board()
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect('/boards')
    
def edit(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'boards/edit.html', {'board': board})
    
def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect('/boards')

def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('/boards')