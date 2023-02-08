from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Question
from django.core.paginator import Paginator
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    question = Question.objects.all
    context = {'question': question}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

#요청게시판
def question(request):
    page = request.GET.get('page','1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10) # 한페이지당 10개씩
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

#요청게시판-게시글등록
@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:question')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

#요청게시판-답글달기
@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo:question_detail.html', context)