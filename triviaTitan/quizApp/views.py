from django.shortcuts import render
from quizApp.models import Quiz 
from quizApp.forms import QuizForm
from django.views.generic import DetailView, View

# Create your views here.
def mainpage_view(request):
    quiz_list = Quiz.objects.all()
    my_dict = {"quiz_list" : quiz_list}
    return render(request, 'quizApp/index.html', context=my_dict)

def quizpage_view(request):
    quiz_list = Quiz.objects.all()
    my_dict = {"quiz_list" : quiz_list}
    return render(request, 'quizApp/quizFile.html', context=my_dict)

def quizcreated_view(request):
    return render(request, 'quizApp/submittedFile.html')

def quizcreator_view(request):
    form = QuizForm()

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            print("Success!!!")
        return quizcreated_view(request)

    return render(request, 'quizApp/quizCreator.html', {'form':form})

 
class QuizPlayView(DetailView):
    model = Quiz
    template_name = 'quizApp/quizFile.html'

def ScoreView(request):
    return render(request, 'quizApp/scoreDisplay.html')