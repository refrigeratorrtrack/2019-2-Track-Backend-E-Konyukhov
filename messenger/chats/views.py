from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def chat_list(request):
    return JsonResponse({'chat1': 'Ivan',
                        'chat2': 'Vlad0S',
                        'chat3': 'Arkadii666'})

def chat(request, chat_id):
    if chat_id not in [1, 2, 3]:
        return JsonResponse({'error': 'not found'})
    else:
        return JsonResponse({'chat': 'messages with {}'.format(['Ivan', 'Vlad0S', 'Arkadii666'][chat_id])})
