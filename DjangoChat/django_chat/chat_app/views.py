from django.shortcuts import render
from .models import ChatRoom, ChatMessage

# Create your views here.
def index(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, 'chat_app/index.html', {'chat_rooms': chat_rooms})

def chat_room(request, slug):
    chat_room = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chat_room)[0:30]
    context = {
        'chat_room': chat_room,
        'messages': messages,}
    return render(request, 'chat_app/room.html', context)
