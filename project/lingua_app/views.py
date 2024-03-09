from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tutor, Student, Flashcard, Subscription
from .forms import TutorLoginForm, StudentLoginForm, SignupForm

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

def tutor_login(request):
    if request.method == 'POST':
        form = TutorLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tutor_dashboard')  # dashboard ka url 
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = TutorLoginForm()
    return render(request, 'tutor_login.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_dashboard')  # student dashboard url
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = StudentLoginForm()
    return render(request, 'student_login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            role = form.cleaned_data['role']
            user.save()
            if role == 'tutor':
                 
                Tutor.objects.create(user=user)
            elif role == 'student':
                
                Student.objects.create(user=user)
            login(request, user)
            return redirect('home')  # Redirect home after signup - udhar dashboard based on role
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})