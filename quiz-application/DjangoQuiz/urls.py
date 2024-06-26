from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from Quiz.views import (
    landing_page, add_question, login_page, logout_page, register_page, home,
    FetchQuestionsView, communication_skills_questions, emotional_intelligence_questions,
    sales_service_questions, ethics_questions, programming_questions, dashboard_view,
    quiz_result, user_management, edit_user, delete_user, course_list, user_list, user_detail, quiz_view,stats
)

urlpatterns = [
    path('', landing_page, name='landingPage'),  # Direct root URL to landing page
    path('addQuestion/', login_required(add_question), name='addQuestion'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),
    path('home/', login_required(home), name='home'),  # Home page accessible only after login
    path('fetch_questions/', login_required(FetchQuestionsView.as_view()), name='fetch_questions'),
    path('communication/', login_required(communication_skills_questions), name='Communication'),
    path('emotion/', login_required(emotional_intelligence_questions), name='emotion'),
    path('sales/', login_required(sales_service_questions), name='Sales'),
    path('ethics/', login_required(ethics_questions), name='ethics'),
    path('programming/', login_required(programming_questions), name='Programming'),
    path('dashboard/', login_required(dashboard_view), name='dashboard'),
    path('result/', login_required(quiz_result), name='result'),
    path('user_management/', login_required(user_management), name='user_management'),
    path('admin/users/edit/<int:user_id>/', login_required(edit_user), name='edit_user'),
    path('admin/users/delete/<int:user_id>/', login_required(delete_user), name='delete_user'),
    path('course_list/', login_required(course_list), name='course_list'),
    path('user_list/', login_required(user_list), name='user_list'),
    path('users/<int:user_id>/', login_required(user_detail), name='user-detail'),
    path('quiz/<str:category>/', login_required(quiz_view), name='quiz_view'),
    path('stats/', login_required(stats), name='stats'),
    # path('api/users/', fetch_users, name='fetch_users'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

