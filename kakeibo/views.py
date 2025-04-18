from django.shortcuts import render, redirect
from .models import Kakeibo
from .forms import KakeiboForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    records = Kakeibo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'kakeibo/home.html', {'records': records})

@login_required
def add_record(request):
    if request.method == 'POST':
        form = KakeiboForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('home')
    else:
        form = KakeiboForm()
    return render(request, 'kakeibo/add.html', {'form': form})
