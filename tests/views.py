from django.shortcuts import render, redirect, get_object_or_404
from random import shuffle
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Question, Answer, Result, QuizModel, Theme

def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('login')

def qiuz(request):
    quizs = QuizModel.objects.all()
    context = {
        'quizs': quizs
    }
    return render(request, 'tests/quiz.html', context)

@login_required(login_url='login')
def quistion(request, pk):
    quistions = Question.objects.filter(quiz_id = pk)
    
    # quistions = (list(quistions))
    answers = Answer.objects.all()
    answers = list(answers)
    shuffle(answers)
    if request.method == "POST":
        correct = 0
        wrong = 0
        for q in quistions:
            if request.POST.get(q.name) == "True":
                correct += 1
            else:
                wrong += 1
            quiz = q.quiz
        if Result.objects.all().filter(user=request.user, quiz=quiz).exists():
            pass
        else:
            timer_value = int(request.POST.get('timer_value', 0))
            Result.objects.create(
                user=User.objects.get(username=request.user.username),
                total_question=len(quistions),
                corrent_question=correct,
                quiz = quiz,
                spend_time=timer_value
            )
        total_ball = round(correct * 100 / len(quistions), 2)
        if total_ball==100:
            tavakkal = 0
            status = "Mavzuni o'qib kelgan bola !"
        elif total_ball>=80:
            tavakkal = 1
            status  = "Ozgina yetmay qoldi lekin zo'r :)"
        elif total_ball==70:
            tavakkal = 2
            status = 'Sizni tavakkal qilganingizni uncha sezmadim lekin bor'
        elif total_ball < 70 and total_ball > 50:
            tavakkal = 3
            status = 'Sekinroq akasi tavakkalni kamroq qiling !'
        elif total_ball == 40:
            tavakkal = 5
            status = "Prosta kirib tavakkal qilib chiqish necha pul bo'layabdi ...?"
        elif total_ball == 30 or total_ball==20 or total_ball == 10 or total_ball==0:
            tavakkal = 8
            status = "Kallangizga qoyil 7 ta yo 9 talar tavkkal bosdingiz o'ziyam"
        else:
            tavakkal = 0
            status = 'undefiend'
        
        context = {
            'pk': pk,
            'correct': correct,
            'wrong': wrong,
            'total_question': len(quistions),
            'user': set(request.user.username),
            'total': round(correct * 100 / len(quistions), 2),
            'tavakkal': tavakkal,
            'status': status
        }
        return render(request, 'tests/result.html', context)
    context = {
        'quistions': quistions,
        'answers': answers,
    }

    return render(request, 'tests/quistion.html', context)

def result_list(request, pk):
    results_base = Result.objects.filter(quiz_id = pk).order_by('-corrent_question')
    context = {
        'results_base': results_base
    }
    return render(request, 'tests/result_detail.html', context)


def themes(request, slug):
    all_theme = get_object_or_404(Theme, slug=slug)
    context = {
        'all_theme': all_theme
    }
    return render(request, 'theme_list.html', context)