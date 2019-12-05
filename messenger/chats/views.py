from django.http import JsonResponse, HttpResponseNotAllowed
from chats.models import Member, Chat, Message
from userprofile.models import User
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
@login_required
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponseNotAllowed(['GET'])

@login_required
def chat_list(request):
    if request.method == 'GET':
        return JsonResponse({'chat1': 'Ivan',
                            'chat2': 'Vlad0S',
                            'chat3': 'Arkadii666'})
    else:
        return HttpResponseNotAllowed(['GET'])

@login_required
def chat(request, chat_id):
    if request.method == 'GET':
        return JsonResponse({'chat': 'messages with {}'.format(['Ivan', 'Vlad0S', 'Arkadii666'][chat_id])})
    else:
        return HttpResponseNotAllowed(['GET'])
