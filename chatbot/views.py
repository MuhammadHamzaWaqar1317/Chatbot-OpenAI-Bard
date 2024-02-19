from bardapi import Bard
from django.shortcuts import render
import openai
import os
from django.http import JsonResponse
import requests
from chatbot.models import Chat

# Create your views here.

os.environ['_BARD_API_KEY'] = "ZgivN-R2C2YPKzeP3Kkx951fZtIUfE7i5c8LBEImMRJWgQEUJY-iOjFpgxkwD0Wc3FsD8A."
token = "ZgivN-R2C2YPKzeP3Kkx951fZtIUfE7i5c8LBEImMRJWgQEU19Q17mr5FQtV5pjz0xuPJA."

openai.api_key="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"


def ask_bard(message):
    session = requests.Session()
    session.headers = {
        "Host": "bard.google.com",
        "X-Same-Domain": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "https://bard.google.com",
        "Referer": "https://bard.google.com/",
    }
    session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))
    #session.cookies.set("__Secure-1PSID", token)

    bard = Bard(token=token, session=session, timeout=30)
    rsp = Bard().get_answer(message)['content']

    print(rsp)
    return rsp


def ask_openai(message):
    response=openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0,
        stop=None,
    )
    print(response)
    answer=response.choices[0].text.strip()
    return answer

def chatbot(request):
    if request.method=='POST':
        message = request.POST.get('message')
        response=ask_openai(message)
        c=Chat(message=message,response=response)
        c.save()
        return JsonResponse({'message':message, 'response': response})
    return render(request, "chatbot.html")

