
from django.shortcuts import render, redirect
from .forms import SubscribeForm
from django.core.mail import send_mail


def newsletter(request):
    """
    Newsletter form request
    """
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            subscriber = form.save()
            subscriber_email = subscriber.email
            send_mail("Welcome!", "Thanks for subcribing.",
                      "sa083850@gmail.com",
                      {subscriber.email},)
            return redirect('newsletter_success')
    else:
        form = SubscribeForm()

    return render(request, 'newsletter/newsletter.html', {'form': form})


def newsletter_success(request):
    """
    """

    return render(request, 'newsletter/newsletter_success.html')
