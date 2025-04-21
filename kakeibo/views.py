from django.shortcuts import render, redirect, get_object_or_404
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


@login_required
def edit_record(request, pk):
    record = get_object_or_404(Kakeibo, pk=pk, user=request.user)
    if request.method == "POST":
        form = KakeiboForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = KakeiboForm(instance=record)
    return render(request, 'kakeibo/edit.html', {'form': form})


@login_required
def delete_record(request, pk):
    record = get_object_or_404(Kakeibo, pk=pk, user=request.user)
    if request.method == "POST":
        record.delete()
        return redirect('home')
    return render(request, 'kakeibo/delete.html', {'record': record})
