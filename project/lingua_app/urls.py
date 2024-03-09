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
    login_page,  # Updated import
    signup,
)

urlpatterns = [
    path('', home, name='home'),
    path('tutors/', TutorListView.as_view(), name='tutor_list'),
    path('tutors/<int:pk>/', TutorDetailView.as_view(), name='tutor_detail'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('flashcards/', FlashcardListView.as_view(), name='flashcard_list'),
    path('flashcards/<int:pk>/', FlashcardDetailView.as_view(), name='flashcard_detail'),
    path('subscriptions/create/', SubscriptionCreateView.as_view(), name='subscription_create'),
    path('subscriptions/<int:pk>/delete/', SubscriptionDeleteView.as_view(), name='subscription_delete'),
    path('login/', login_page, name='login'),  # Updated path for login
    path('signup/', signup, name='signup'),
]
