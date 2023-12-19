from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product


@login_required
def show_likes(request):
    """ A view to show the user's favorite products"""
    liked_products = Product.objects.filter(users_likes=request.user)

    context = {
        'liked_products': liked_products,
    }

    return render(request, 'likes/likes.html', context)


@login_required
def add_or_remove_likes(request, product_id):
    """ Add product to the user's favorites """
    product = get_object_or_404(Product, id=product_id)

    if product.users_likes.filter(id=request.user.id).exists():
        product.users_likes.remove(request.user)
        messages.success(request,
                         f'{product.name} has been \
                         removed from your favorites.')
    else:
        product.users_likes.add(request.user)
        messages.success(request,
                         f'{product.name} has been \
                         added to your favorites.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))