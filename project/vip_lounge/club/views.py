from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def lobby(request):
    return render(request, 'lobby.html')
@login_required
def member_lounge(request):
    return render(request, 'member_lounge.html')
