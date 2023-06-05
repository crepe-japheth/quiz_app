import json
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.generic import ListView

from .models import (
    Quiz,
    Question,
    Result
)


def index(request):
    return render(request, 'quiz_app/index.html')

def about(request):
    return render(request, 'quiz_app/about.html')

def contact(request):
    return render(request, 'quiz_app/contact.html')

def appointment(request):
    return render(request, 'quiz_app/appointment.html')

def courses(request):
    return render(request, 'quiz_app/courses.html')

def feature(request):
    return render(request, 'quiz_app/feature.html')

def team(request):
    return render(request, 'quiz_app/team.html')

def not_found(request):
    return render(request, 'quiz_app/404.html')

def testimonial(request):
    return render(request, 'quiz_app/testimonial.html')

class QuizListView(ListView):
    model = Quiz
    template_name = "quiz_app/main.html"


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    context = {"quiz":quiz}
    return render(request, 'quiz_app/quiz.html', context)


def save_quiz_view(request, pk):
    if request.method == 'POST':
        quiz = Quiz.objects.get(pk=pk)
        answers = []
        score = 0
        status = ''
        data_ = json.loads(request.body)
        for question, answer in data_.items():
            question_ = Question.objects.get(text=question)
            a_list = list(question_.get_answers)
            ans_list = [correct_answer.text for correct_answer in list(filter(lambda n: n.correct == True, a_list))]
            for ans in ans_list:
                if answer != None:
                    for ch in answer:
                        if ans == ch:
                            score += (1/len(ans_list))
            answers.append({question : {'correct_answer':ans_list, 'answered':answer}})
        score = (score * 100) / quiz.number_of_questions 
        if score < quiz.required_score_to_pass:
            status = "Failed"
        else:
            status = "Passed"           
        return JsonResponse({"answers":answers, "scored":score, "status":status})


def result(request):
    result = Result.objects.all()
    context = {'result' : result}
    return render(request, 'quiz_app/result.html', context)

def login_view(request):
    return render(request, 'quiz_app/login.html')

def signup_view(request):
    return render(request, 'quiz_app/signup.html')
