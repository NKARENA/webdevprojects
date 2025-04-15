from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('<h1>Hello World from CBV</h1>')


class HelloWorldTemplateView(TemplateView):
    template_name = 'testAppTem/results.html'
    
class HelloWorldTemplateContext(TemplateView):
    template_name = 'testAppTem/info.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Shaw"
        context['subject'] = 'Python'
        context['marks'] = '97'
        return context
