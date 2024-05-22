from django.http import HttpResponse
from django.db.models import Count, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone

from .models import Recruiter, MessageThread, Message

# Hardcode for logged in as recruiter
RECRUITER_ID = 125528

def inbox(request):
    recruiter = Recruiter.objects.get(id = RECRUITER_ID)
    threads = MessageThread.objects.filter(recruiter = recruiter).select_related('candidate', 'job')[:30]

    _context = { 'title': "Djinni - Inbox", 'recruiter': recruiter, 'threads': threads }

    return render(request, 'inbox/chats.html', _context)

def inbox_thread(request, pk):
    thread = MessageThread.objects.get(id = pk)
    messages = thread.message_set.all().order_by('created')

    _context = {
        'pk': pk,
        'title': "Djinni - Inbox",
        'thread': thread,
        'messages': messages,
        'candidate': thread.candidate,
    }

    if request.method == 'POST':
        reply_msg = request.POST.get('reply_msg')
        if reply_msg:
            thread = get_object_or_404(MessageThread, id=pk)
            new_message = Message(
                body=reply_msg,
                created=timezone.now(),
                sender=Message.Sender.RECRUITER,
                recruiter=thread.recruiter,
                candidate=thread.candidate,
                thread=thread
            )
            new_message.save()
            thread.last_updated = timezone.now()
            thread.save()

    return render(request, 'inbox/thread.html', _context)
