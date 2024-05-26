from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from.forms import addQuestionform
from.models import QuesModel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse 
import logging

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
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
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




# View to fetch questions based on category
# @csrf_exempt
# Assuming this is the view function for fetching questions based on category
# Configure logging
logger = logging.getLogger(__name__)

def fetch_questions(request):
    if request.method == 'POST' and 'category' in request.POST:
        category = request.POST['category']
        logger.info(f'Retrieving questions for category: {category}')  # Log the category being queried
        
        questions = QuesModel.objects.filter(category=category)
        logger.debug(f'Fetched {len(questions)} questions.')  # Log the number of questions fetched
        
        questions_data = [{'question': q.question, 'option1': q.option1, 'option2': q.option2, 'option3': q.option3, 'option4': q.option4} for q in questions]
        
        # Include category in the response data
        response_data = {'category': category, 'questions': questions_data}
        
        # Optionally, log the response data before returning it
        logger.debug(f'Returning response data: {response_data}')
        
        return JsonResponse(response_data)
    else:
        logger.error('Invalid request method or missing category parameter.')
        return JsonResponse({'error': 'Invalid request method or missing category parameter.'})

# Helper function to fetch and render questions by category
def get_questions_by_category(request, category):
    questions = QuesModel.objects.filter(category=category)
    context = {'questions': questions}
    return render(request, f'Quiz/{category.lower().replace(" ", "_")}.html', context)

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


