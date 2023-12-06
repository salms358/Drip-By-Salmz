
from django.shortcuts import render, redirect
from .forms import SubscribeForm

def newsletter(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can send a confirmation email here
            return redirect('newsletter_success')  # Redirect to the success page
    else:
        form = SubscribeForm()

    return render(request, 'newsletter/newsletter_success.html', {'form': form})

def newsletter_success(request):
    return render(request, 'newsletter/newsletter_success.html')
