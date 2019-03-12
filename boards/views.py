import pprint
from django.shortcuts import render, HttpResponse, redirect
from .models import Board, Comment

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
    
def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    comments = board.comment_set.all()
    context = {
        'board': board,
        'comments': comments
    }
    return render(request, 'boards/detail.html', context)
    
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
    
def edit(request, board_pk):
    if request.method == 'POST':
        board = Board.objects.get(pk=board_pk)
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

def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == "POST":
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:index')
        
def comments_create(request, board_pk):
    # 1. 댓글 달 게시물을 가져온다.
    board = Board.objects.get(pk=board_pk)
    # 2. 댓글을 저장한다.
    comment = Comment()
    comment.content = request.POST.get('content')
    comment.board = board
    comment.save()
    return redirect('boards:detail', comment.board_id)
    

    