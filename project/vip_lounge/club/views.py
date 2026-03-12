from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

def lobby(request):
    return render(request, 'lobby.html')
@login_required
def member_lounge(request):
    return render(request, 'member_lounge.html')
@permission_required('club.view_CustomUser', raise_exception=True)
def manager_office(request):
    return render(request, 'manager_office.html')
