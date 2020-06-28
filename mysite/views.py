from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse
import json
from .form import NewForm
import main
from main.models import Question
from django.views.decorators.csrf import csrf_exempt
from .serializers import QuestionSerializer
from rest_framework import generics

@csrf_exempt
def get_response(request):
    response = {'status': None}
    qs = Question.objects.all()
    print(qs)
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        message = data['message']
        print(response)
        answer = "Sorry no answer for that. If you want to add a Question, press add!"
        for row in qs.values_list():
            print(row[1])
            if row[1].lower() == message.lower():
                answer = row[2]
        response['message'] = {'text': answer, 'user': False, 'chat_bot': True}
        response['status'] = 'ok'

    else:
        response['error'] = 'no data'

    print(response)
    return HttpResponse(
        json.dumps(response),
        content_type="application/json"
    )

def get_sentence(request, sentence):
    response = {'status': None}
    qs = Question.objects.all()
    print(qs)
    if request.method == 'GET':
        message = sentence
        print(response)
        answer = "Sorry no answer for that. If you want to add a Question, press add!"
        for row in qs.values_list():
            print(row[1])
            if row[1].lower() == message.lower():
                answer = row[2]
        response['message'] = {'text': answer, 'user': False, 'chat_bot': True}
        response['status'] = 'ok'

    else:
        response['error'] = 'no data'

    print(response)
    return HttpResponse(
        json.dumps(response),
        content_type="application/json"
    )



def home(request):
    context = {'title': 'Django Chatbot'}
    return render(request,'home.html', context)

def question_add(request):
    if request.method=='POST':
        form = NewForm(request.POST)
        if form.is_valid():

            qs = Question()
            qs.question_text = form.cleaned_data['question']
            qs.answer = form.cleaned_data['answer']
            qs.save()

            return redirect('/')

    else:
        form = NewForm()
        print("pressed")


    return render(request,'new_question.html', {'form':form})


class QuestionAPI(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

