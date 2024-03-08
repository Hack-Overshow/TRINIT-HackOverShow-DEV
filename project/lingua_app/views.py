from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tutor, Student, Flashcard, Subscription

def home(request):
    return render(request, 'index.html')

class TutorListView(ListView):
    model = Tutor
    template_name = 'tutor_list.html'
    context_object_name = 'tutors'

class TutorDetailView(DetailView):
    model = Tutor
    template_name = 'tutor_detail.html'
    context_object_name = 'tutor'

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'

class FlashcardListView(ListView):
    model = Flashcard
    template_name = 'flashcard_list.html'
    context_object_name = 'flashcards'

class FlashcardDetailView(DetailView):
    model = Flashcard
    template_name = 'flashcard_detail.html'
    context_object_name = 'flashcard'

class SubscriptionCreateView(CreateView):
    model = Subscription
    fields = ['student', 'tutor']  # Add more fields as needed
    template_name = 'subscription_form.html'

    def form_valid(self, form):
        # Perform any additional operations if needed
        return super().form_valid(form)

class SubscriptionDeleteView(DeleteView):
    model = Subscription
    template_name = 'subscription_confirm_delete.html'
    success_url = '/subscriptions/'  # Redirect URL after deletion
