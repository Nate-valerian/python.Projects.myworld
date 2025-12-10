# Backup current file

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    return render(request, 'all_members.html', {'mymembers': mymembers})

def details(request, id):
    mymember = Member.objects.get(id=id)
    return render(request, 'details.html', {'mymember': mymember})

def main(request):
    return render(request, 'main.html')

