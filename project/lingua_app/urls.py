from django.contrib import admin
from django.urls import path
from .views import (
    home,
    TutorListView,
    TutorDetailView,
    StudentListView,
    StudentDetailView,
    FlashcardListView,
    FlashcardDetailView,
    SubscriptionCreateView,
    SubscriptionDeleteView,
    tutor_login,  # Import tutor_login view
    student_login,  # Import student_login view
    signup,
)

urlpatterns = [
    path('', home),
    path('tutors/', TutorListView.as_view(), name='tutor_list'),
    path('tutors/<int:pk>/', TutorDetailView.as_view(), name='tutor_detail'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('flashcards/', FlashcardListView.as_view(), name='flashcard_list'),
    path('flashcards/<int:pk>/', FlashcardDetailView.as_view(), name='flashcard_detail'),
    path('subscriptions/create/', SubscriptionCreateView.as_view(), name='subscription_create'),
    path('subscriptions/<int:pk>/delete/', SubscriptionDeleteView.as_view(), name='subscription_delete'),
    path('tutor/login/', tutor_login, name='tutor_login'),  # Add tutor login path
    path('student/login/', student_login, name='student_login'),  # Add student login path
    path('signup/', signup, name='signup'),

]
