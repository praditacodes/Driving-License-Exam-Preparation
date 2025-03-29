from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import createuserform, addQuestionform, ProfileUpdateForm
from .models import QuesModel, QuizResult
from django.contrib.auth.decorators import login_required
import time
from django.core.paginator import Paginator
from .models import QuesModel  
import random
# Assuming you have the correct Question model for random question functionality
# Home page with quiz functionality
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import QuesModel

# Leaderboard
def leaderboard(request):
    leaders_list = QuizResult.objects.order_by('-score')  # Fetch all scorers sorted by score
    paginator = Paginator(leaders_list, 10)  # Show 10 per page
    page_number = request.GET.get('page')
    leaders = paginator.get_page(page_number)
    return render(request, 'leaderboard.html', {'leaders': leaders})

# User registration page
def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = createuserform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    
    return render(request, 'register.html', {'form': form})

# User login page
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    
    return render(request, 'login.html')

# Helper function to calculate the quiz result
def calculate_quiz_result(questions, post_data):
    score = 0
    correct = 0
    wrong = 0
    total = 0

    for q in questions:
        total += 1
        answer = post_data.get(f"q_{q.id}")  # This gets the answer from the POST data
        if answer == q.correct_answer:  # Change 'ans' to 'correct_answer'
            score += 10
            correct += 1
        else:
            wrong += 1

    percent = (score / (total * 10)) * 100 if total > 0 else 0

    return score, correct, wrong, percent, total

# List of all quizzes
def quiz_list(request):
    quizzes = QuesModel.objects.all()  # Fetch all quizzes
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

# Display quiz details for a specific quiz
def quiz_detail(request, pk):
    quiz = get_object_or_404(QuesModel, pk=pk)  # Fetch quiz by pk
    return render(request, 'quiz_detail.html', {'quiz': quiz})

# Start the quiz for a specific quiz
def start_quiz(request, pk):
    quiz = get_object_or_404(QuesModel, pk=pk)
    questions = quiz.quesmodel_set.all()  # Assuming a reverse relationship
    start_time = time.time()

    context = {
        'quiz': quiz,
        'questions': questions,
        'start_time': start_time,
        'total_questions': questions.count(),
    }

    return render(request, 'quiz_start.html', context)

# Submit the quiz after the user has answered the questions
def submit_quiz(request, pk):
    if request.method == 'POST':
        quiz = get_object_or_404(QuesModel, pk=pk)
        questions = quiz.quesmodel_set.all()

        score, correct, wrong, percent, total = calculate_quiz_result(questions, request.POST)

        start_time = float(request.POST.get('start_time'))
        time_taken = round(time.time() - start_time, 2)

        result = QuizResult.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            correct_answers=correct,
            incorrect_answers=wrong,
            percentage=percent,
            total_questions=total,
            time_taken=time_taken
        )
        
        return render(request, 'result.html', {
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
            'time_taken': time_taken,
            'quiz': quiz,
        })

# Show the results of the quiz after submission
@login_required(login_url='login') 
def quiz_results(request):
    if request.user.is_authenticated:
        results = QuizResult.objects.filter(user=request.user).order_by('-id')[:1]
        return render(request, 'result.html', {'results': results})
    return redirect('login')





def home(request):
    # Fetch all questions and order them
    questions_list = QuesModel.objects.all().order_by('id')  # Replace 'id' with your preferred field
    paginator = Paginator(questions_list, 10)  # Show 10 questions per page

    # Get the current page number from the request's query parameters
    page_number = request.GET.get('page')
    
    # Get the corresponding page of questions
    questions = paginator.get_page(page_number)

    if request.method == 'POST':
        # Process the form data after quiz submission
        score, correct, wrong, percent, total = calculate_quiz_result(questions_list, request.POST)

        # Render the result page with calculated score and stats
        return render(request, 'result.html', {
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
        })

    # If it's a GET request, render the quiz page with paginated questions
    return render(request, 'home.html', {'questions': questions})



# View to add a new question (only accessible by staff users)
@login_required
def add_question(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == "POST":
        form = addQuestionform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = addQuestionform()

    return render(request, 'add_question.html', {'form': form})

# View for random 25 questions from the Question model
def random_questions_view(request):
    all_questions = QuesModel.objects.all()
    selected_questions = random.sample(list(all_questions), 25)

    if request.method == 'POST':
        score = 0
        for idx, question in enumerate(selected_questions):
            user_answer = request.POST.get(f'question_{idx+1}')
            if user_answer == question.correct_answer:
                score += 1
        
        return render(request, 'result.html', {'score': score})

    return render(request, 'random_questions.html', {'questions': selected_questions})
