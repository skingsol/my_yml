from django.shortcuts import render, redirect, get_object_or_404

# from .models import My_yml
# from .forms import My_yml


def chart(request):
    return render(request, "my_yml/chart.html")


def total1(request):
    return render(request, "my_yml/today_total.html")


def test2(request):
    return render(request, "my_yml/test2.html")


# def todo_list(request):

#     # 전체목록 가져오기
#     # todos = Todo.objects.all()

#     # 미완료된 목록만 가져오기
#     todos = Todo.objects.filter(complete=False)

#     # templates/todo/todo_list.html
#     return render(request, "todo/todo_list.html", {"todos":todos})


# def todo_detail(request, id):
#     # id와 일치하는 todo 조회 후 보내기
#     todo = get_object_or_404(Todo, id=id)

#     return render(request, "todo/todo_detail.html", {"todo":todo})


# def todo_create(request):
#     """
#     get / post 둘 다 동작
#     """
#     if request.method == "POST":
#         form = TodoForm(request.POST)   # DTO 개념
#         if form.is_valid(): # 유효성 검증(테이블 작성 기준)
#             todo = form.save() # DB 반영
#             return redirect("todo_detail", id=todo.id)

#     else:
#         # 화면단에서 사용 가능함
#         form = TodoForm()

#     return render(request, "todo/todo_create.html", {"form":form})

# def todo_edit(request, id):
#     # id와 일치하는 todo 찾기
#     todo = get_object_or_404(Todo, id = id)

#     # post - 바인딩 된 폼에 post 요청으로 넘어오는 값 담기
#     if request.method == "POST":
#         form = TodoForm(request.POST, instance=todo)
#         if form.is_valid():
#             form.save()
#             return redirect("todo_detail", id=todo.id)
#     else:
#         # get - 찾은 todo를 폼에 바인딩 한 후 보내기
#         form = TodoForm(instance = todo)
#     return render(request, "todo/todo_edit.html",{"form":form})

# def todo_done(request, id):
#     # 수정할 todo 찾기
#     # todo = get_object_or_404(Todo, id=id)
#     todo = Todo.objects.get(id=id)
#     # 수정할 todo 값 변경
#     todo.complete = True
#     todo.save()
#     return redirect("todo_list")

# def done_list(request):
#     # 완료된 목록 가져오기
#     # where complete = 1
#     dones = Todo.objects.filter(complete=True)

#     return render(request, "todo/done_list.html", {"dones":dones})
