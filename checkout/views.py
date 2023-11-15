from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O0rzkBvgmz6lyaoDxvpMu6xhG9N88s1D7tn27PVDfaURWqYN7u7fE5lpMiA2tzS1igcNGkYvwtroiAT32L1dQ5500lBRDk7r7',
        'client_secret': 'sk_test_51O0rzkBvgmz6lyaoTfDMc0JRM57ZCUkrutpNEnuTXjfZSfFjatCU7hCOkxYlGAEsVz1bs1QlluiMw9ZL3NggPVDC00j84M544J',
    }

    return render(request, template, context)