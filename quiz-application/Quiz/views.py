import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import addQuestionform
from .forms import createuserform
from .models import QuesModel
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from django.contrib.auth.models import User
from.models import UserProfile, QuizAttempt
from datetime import timedelta
from django.utils import timezone

# Initialize logger
logger = logging.getLogger('DjangoQuiz')  # Use the logger name defined in your settings

# Landing page view
def landing_page(request):
    return render(request, 'Quiz/index.html')

def dashboard_view(request):
    return render(request, 'Quiz/dashboard.html')

# View for user login
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                # Ensure UserProfile exists
                UserProfile.objects.get_or_create(user=user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            form = AuthenticationForm()
        
        context = {'form': form}
        return render(request, 'Quiz/login.html', context)

# View for user registration
def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to the homepage if the user is already authenticated
    else:
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                form.save()  # Save the new user
                messages.success(request, "Registration successful! Please log in.")
                return redirect('login')  # Redirect to the login page
        context = {'form': form}
        return render(request, 'Quiz/register.html', context)

    
# View to add a new question
def add_question(request):
    if request.user.is_staff:
        form = addQuestionform()
        if request.method == 'POST':
            form = addQuestionform(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Question added successfully.")
                return redirect('home')
            else:
                messages.error(request, "There was an error adding the question. Please try again.")
        context = {'form': form}
        return render(request, 'Quiz/addQuestion.html', context)
    else:
        return redirect('home')
    
# View to handle logout
def logout_page(request):
    logout(request)
    return redirect('/')

def home(request):
    if request.method == 'POST':
        # Process POST request
        print("Processing POST request...")
        # Placeholder for processing logic
        # Assuming you want to redirect or return some response after processing POST
        return HttpResponse("POST request processed")  # Or use redirect or render as needed
    else:
        # Render the home page with categories
        print("Rendering home page...")
        context = {'categories': ['Programming', 'Communication', 'Emotion', 'Ethics', 'Sales']}
        return render(request, 'Quiz/home.html', context)

class FetchQuestionsView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            category = data.get('category')
            if category:
                # Trim the trailing slash from the category
                trimmed_category = category.rstrip('/')
                
                # Query the database using the trimmed category
                questions = QuesModel.objects.filter(category=trimmed_category)
                questions_data = [{'question': q.question, 'option1': q.option1, 'option2': q.option2, 'option3': q.option3, 'option4': q.option4} for q in questions]
                response_data = {'category': trimmed_category, 'questions': questions_data}
                return JsonResponse(response_data)
            else:
                return JsonResponse({'error': 'Category not provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            logger.error("Error fetching questions: %s", str(e))
            return JsonResponse({'error': 'An unknown error occurred'}, status=500)

# Helper function to fetch and render questions by category
def get_questions_by_category(request, category):
    # Trim the trailing slash from the category
    trimmed_category = category.rstrip('/')
    
    # Query the database using the trimmed category
    questions = QuesModel.objects.filter(category=trimmed_category)
    context = {'questions': questions}
    return render(request, f'Quiz/{trimmed_category.lower().replace(" ", "_")}.html', context)

# Views for specific categories of questions
def communication_skills_questions(request):
    return get_questions_by_category(request, 'communication')

def emotional_intelligence_questions(request):
    return get_questions_by_category(request, 'emotional')

def sales_service_questions(request):
    return get_questions_by_category(request, 'sales')

def programming_questions(request):
    return get_questions_by_category(request, 'programming')

def ethics_questions(request):
    return get_questions_by_category(request, 'ethics')





# views.py
def quiz_view(request, category):
    questions = QuesModel.objects.filter(category=category)
    if not questions.exists():
        logger.warning("No questions found for category %s", category)
    else:
        logger.info("Fetched %d questions for category %s", questions.count(), category)
    context = {
        'questions': questions,
        'selected_category': category,
    }
    return render(request, f'Quiz/{category.lower()}.html', context)

def quiz_result(request):
    if request.method == 'POST':
        logger.info("Submitted data: %s", request.POST)

        category = request.POST.get('category', 'Unknown')
        logger.info("Category: %s", category)

        question_ids = [key[8:] for key in request.POST.keys() if key.startswith('question')]
        questions = QuesModel.objects.filter(id__in=question_ids)
        logger.debug("Fetched questions: %s", questions)

        if not questions.exists():
            logger.error("No questions found for the provided IDs.")
            return redirect('home')

        score = 0
        wrong = 0
        correct = 0
        total = 0

        for q in questions:
            total += 1
            user_answer = request.POST.get(f"question{q.id}")
            correct_answer = q.answer

            if correct_answer == user_answer:
                score += 10
                correct += 1
            else:
                wrong += 1

        percent = round(score / (total * 10) * 100) if total > 0 else 0

        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.total_score += score
        user_profile.num_tests_taken += 1
        user_profile.save()

        QuizAttempt.objects.create(
            user_profile=user_profile,
            category=category,
            score=score
        )

        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }

        return render(request, 'Quiz/result.html', context)
    else:
        return redirect('home')

def create_quiz_attempt(user_profile, category, score):
    QuizAttempt.objects.create(
        user_profile=user_profile,
        category=category,
        score=score
    )


# Fetch users
def user_management(request):
    users = User.objects.all()
    return render(request, 'Quiz/user_management.html', {'users': users})

def course_list(request):
    return render(request, 'Quiz/course_list.html')


# Edit user (using POST to update user details)
@csrf_exempt
def edit_user(request, user_id):
    if request.method == 'POST':
        try:
            user = get_object_or_404(User, pk=user_id)
            user.first_name = request.POST.get('first_name', user.first_name)
            user.last_name = request.POST.get('last_name', user.last_name)
            user.email = request.POST.get('email', user.email)
            user.save()
            return JsonResponse({'success': True, 'message': 'User details updated successfully.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

# Delete user
@csrf_exempt
def delete_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_id)
        user.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})



def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'Quiz/user_list.html', {'users': users})
        
def user_detail(request, user_id):
            user_profile = get_object_or_404(UserProfile, pk=user_id)
            quizzes_taken = user_profile.quizzes_taken.all()

            # Debugging: Print quiz attempts to the console
            for quiz in quizzes_taken:
                print(f"Category: {quiz.category}, Score: {quiz.score}")
            return render(request, 'Quiz/user_detail.html', {'user_profile': user_profile})


def stats(request):
    try:
        # Active Users: Count of users who have logged in within the last 30 days
        active_users = User.objects.filter(last_login__gte=timezone.now() - timedelta(days=30)).count()

        # New Signups: Count of users who signed up within the last 30 days
        new_signups = User.objects.filter(date_joined__gte=timezone.now() - timedelta(days=30)).count()

        # Courses Available: Count of courses available (replace with your actual model)
        courses_available = Course.objects.count()

        # Quizzes Taken: Count of all quizzes taken
        quizzes_taken = QuizAttempt.objects.count()

        context = {
            'active_users': active_users,
            'new_signups': new_signups,
            'courses_available': courses_available,
            'quizzes_taken': quizzes_taken
        }

        # Log the context for debugging
        logger.info("Stats context: %s", context)

        return render(request, 'Quiz/home.html', context)

    except Exception as e:
        logger.error("Error in stats view: %s", str(e))
        # Handle errors gracefully, e.g., return an error page or redirect
        return render(request, 'Quiz/error.html', {'error_message': 'An error occurred'})
