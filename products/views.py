from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from .forms import ProductForm
from comments.models import Comment

# Create your views here.


from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Product, Category

from django.http import HttpResponse

from django.db.models import Q


def all_products(request):
    """A view to show all products, including sorting and search queries."""

    # Retrieve all products
    products = Product.objects.all()

    # Initialize variables
    query = None
    categories = None
    sort = None
    direction = None

    # Retrieve all categories
    categories = Category.objects.all()

    # Check if there's a GET request
    if request.GET:

        # Handle sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Handle category filtering
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(categories__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Handle search query
        if 'q' in request.GET:
            query = request.GET['q']
            if query:
                # Filter products by name or description containing the query
                queries = (Q(name__icontains=query) |
                           Q(description__icontains=query))
                products = products.filter(queries)
            else:
                messages.error(request, "You didn't enter a search criteria!")
                return redirect('products')

    # Create a dictionary to store unique products based on primary key
    unique_products_dict = {}
    for product in products:
        unique_products_dict[product.pk] = product

    unique_products = list(unique_products_dict.values())

    # Construct context data
    current_sorting = f'{sort}_{direction}'
    context = {
        'products': unique_products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    comments = Comment.objects.filter(product=product_id)

    context = {
        'product': product,
        'product_comments': comments
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers have access to this!')
        return redirect(reverse, ('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # Set the product's categories based on the selected ones in the
            # form
            selected_categories = request.POST.getlist('categories')
            product.categories.set(selected_categories)

            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update ensure form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Only superusers have access to this feature!')
        return redirect(reverse, ('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
