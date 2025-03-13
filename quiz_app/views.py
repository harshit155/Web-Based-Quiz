from django.shortcuts import render, redirect
from .models import Quiz, Question, Score
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt

class CustomLoginView(LoginView):
    template_name = "registration/login.html"

@login_required
@csrf_exempt
def take_quiz(request):
    quizzes = Quiz.objects.all()  
    questions = Question.objects.all()  

    if request.method == "POST":
        quiz_id = request.POST.get("quiz_id")
        quiz = Quiz.objects.get(id=quiz_id)
        score = 0

        for question in quiz.question_set.all():
            user_answer = request.POST.get(f"question_{question.id}")
            correct_answer = question.correct_answer  
            
            print(f"Question: {question.text}")
            print(f"User Answer: {user_answer}, Correct Answer: {correct_answer}")  


            if user_answer and user_answer.strip().upper() == correct_answer.strip().upper():
                score += 1  

        
        Score.objects.create(user=request.user, quiz=quiz, score=score)

        return redirect("view_score")  

    return render(request, "take_quiz.html", {"quizzes": quizzes, "questions": questions})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Quiz
from .forms import QuizForm

@login_required
def add_quiz(request):
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.created_by = request.user
            quiz.save()
            return redirect("admin_dashboard")
    else:
        form = QuizForm()
    return render(request, "add_quiz.html", {"form": form})

@login_required
def view_score(request):
    scores = Score.objects.filter(user=request.user)
    return render(request, "view_score.html", {"scores": scores})

@login_required
def userdashboard(request):
    return render(request, "userdashboard.html") 

@login_required
def custom_redirect(request):
    return redirect("userdashboard")

def index(request):
    """Renders the login selection page"""
    return render(request, "index.html")

def admin(request):
    """Redirects to Django's default admin login page"""
    return redirect("/admin/")

def login(request):
    return redirect("/login/")
