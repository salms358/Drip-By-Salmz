from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Comment
from .forms import CommentForm

@login_required
def show_comments(request):
    """ A view to show the user's product reviews """
    comments = Comment.objects.filter(author=request.user)

    template = 'comments/comments.html'

    context = {
        'comments': comments,
    }

    return render(request, template, context)

@login_required
def add_comment(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_comments = Comment.objects.filter(author=request.user, product=product)

    if user_comments:
        messages.error(request, 'A review has already been submitted for this product.')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        if request.method == 'POST':
            form = CommentForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.author = request.user
                form.instance.product = product
                form.save()
                messages.success(request, 'Your comment has been submitted')
                update_comment(product)
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to submit the comment. Please ensure the form is valid.')
        else:
            form = CommentForm()

        template = 'comments/add_comment.html'
        context = {
            'product': product,
            'form': form,
        }
        return render(request, template, context)




@login_required
def edit_comment(request, comment_id):
    """ Display form to edit a review """
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, 'You are not authorized to edit this comment.')
        return redirect(reverse('product_detail', args=[comment.product.id]))

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your comment!')

            update_comment(comment.product)

            return redirect(reverse('product_detail',
                            args=[comment.product.id]))
        else:
            messages.error(request, 'Failed to update your comment. \
                Please ensure the form is valid.')
    else:
        form = CommentForm(instance=comment)
        messages.info(request, f'You are editing your comment for \
            {comment.product.name}')

    template = 'comments/update_comment.html'

    context = {
        'form': form,
        'comment': comment,
    }

    return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    """ Delete an existing review """
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, 'You are not authorized \
            to delete this comment.')
        return redirect(reverse('product_detail', args=[comment.product.id]))

    comment.delete()
    messages.success(request, 'Your comment has been deleted!')
    print('COMMENT', comment)
    update_comment(comment.product)

    return redirect(reverse('product_detail', args=[comment.product.id]))


def update_comment(product):
    """ Update the rating field for the product """

    total_comments = Comment.objects.filter(product=product)
    nr_of_total_comments = total_comments.count()
    ratings_sum = 0

    if nr_of_total_comments <= 0:
        product.rating = None
    else:
        for comment in total_comments:
            ratings_sum += comment.rating

        product.rating = ratings_sum / nr_of_total_comments

    product.save()
