from django.contrib import admin
from django.urls import path
from Quiz.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from Quiz.views import FetchQuestionsView
# from Quiz.views import admin_user_list, edit_user, delete_user

urlpatterns = [
    path('', landing_page, name='landingPage'),  # Direct root URL to landing page
    path('addQuestion/', add_question, name='addQuestion'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),
    path('home/', login_required(home), name='home'),  # Home page accessible only after login
    path('fetch_questions/', FetchQuestionsView.as_view(), name='fetch_questions'),
    path('communication/', communication_skills_questions, name='Communication'),
    path('emotion/', emotional_intelligence_questions, name='emotion'),
    path('sales/', sales_service_questions, name='Sales'),
    path('ethics/', ethics_questions, name='ethics'),
    path('programming/', programming_questions, name='Programming'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('result/', quiz_result, name='result'),
    path('admin_user_list/', admin_user_list, name='admin_user_list'),
    path('admin/users/edit/<int:user_id>/', edit_user, name='edit_user'),
    path('admin/users/delete/<int:user_id>/', delete_user, name='delete_user'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
