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

# Initialize logger
logger = logging.getLogger('DjangoQuiz')  # Use the logger name defined in your settings

# Landing page view
def landing_page(request):
    return render(request, 'Quiz/landingPage.html')

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
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        context = {}
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




def quiz_result(request):
    if request.method == 'POST':
        # Log all submitted data
        logger.info("Submitted data: %s", request.POST)

        # Extract question IDs from POST data keys that start with 'question'
        question_ids = [key[8:] for key in request.POST.keys() if key.startswith('question')]

        # Fetch questions based on extracted IDs
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

        # Round off the percent to the nearest whole number
        percent = round(score / (total * 10) * 100) if total > 0 else 0

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
