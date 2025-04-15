from django import forms
from quizApp.models import Quiz

class QuizForm(forms.ModelForm):
	class Meta:
		model = Quiz
		fields = "__all__"