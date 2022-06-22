from django.shortcuts import render, HttpResponse
from .forms import CaptchaForm

def IndexView(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        if form.is_valid():
            return HttpResponse("خوش اومدید")
        else:
            return HttpResponse("(: خوش نیومدید")
    else:
        form = CaptchaForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)