from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testApp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request, 'testAppTem/home.html')

@login_required
def java_exam_view(request):
    return render(request, 'testAppTem/javaExams.html')

@login_required
def python_exam_view(request):
    return render(request, 'testAppTem/pythonExams.html')

@login_required
def aptitude_exam_view(request):
    return render(request, 'testAppTem/aptitudeExams.html')

def logout_view(request):
    return render(request, 'testAppTem/thankyou.html')

def sign_up_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect("/accounts/login")
    return render(request, 'testAppTem/signupform.html', {"form": form})