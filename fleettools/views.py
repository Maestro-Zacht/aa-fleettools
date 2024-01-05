from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return redirect('fleettools:fleetmover')


@login_required
def fleetmover(request):
    return render(request, 'fleettools/fleetmover.html')
