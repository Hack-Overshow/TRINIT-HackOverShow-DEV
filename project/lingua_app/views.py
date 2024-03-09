from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Tutor, Student, Flashcard, Subscription
from .forms import SignupForm, LoginForm, MeetingCreateForm
from django.contrib.auth.decorators import login_required


@login_required()  # to ensure only logged in user can view this page.
def meeting_list(request):
    """We are going to filter the meeting, so only the registered user can view
    the page, and then all meeting created by such individual will be displayed"""
    user = request.user
    meetings = Meeting.objects.filter(creator=user) 

    return render(request, 'project/templates/meeting_list.html', {'meetings': meetings})


def call(request):
    form = MeetingCreateForm()
    return render(request, 'onlinemeet/call.html', {'form': form})

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
    fields = ['student', 'tutor']   
    template_name = 'subscription_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

class SubscriptionDeleteView(DeleteView):
    model = Subscription
    template_name = 'subscription_confirm_delete.html'
    success_url = '/subscriptions/'  # Redirect wala idhar
 

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data['role']  # Assign role from form data
            user.save()
            login(request, user)  # Log in the user after signup
            return redirect('home')  # Redirect to home page after signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})