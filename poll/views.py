from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
def create(request):
    return render(request, 'create.html')
def base(request):
    return render(request, 'base.html',)
def result(request, poll_id):
    return render(request, 'result.html',)
def vote(request, poll_id):
    return render(request, 'vote.html',)
