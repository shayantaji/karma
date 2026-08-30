from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from order.models import Order, OrderDetail
from product.models import Product


# Create your views here.


def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))
    if count < 1:
        # count = 1
        return JsonResponse({
            'status': 'invalid_count',
            'text': 'مقدار وارد شده معتبر نمی باشد',
            'confirm_button_text': 'مرسی از شما',
            'icon': 'warning'
        })

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_deleted=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += count
                current_order_detail.final_price = product.final_price
                current_order_detail.save()
            else:
                new_detail = OrderDetail(
                    order_id=current_order.id,
                    product_id=product_id,
                    final_price=product.final_price,
                    count=count
                )
                new_detail.save()

            return JsonResponse({
                'status': 'success',
                'text': 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد',
                'confirm_button_text': 'باشه ممنونم',
                'icon': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'text': 'محصول مورد نظر یافت نشد',
                'confirm_button_text': 'مرسییییی',
                'icon': 'error'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای افزودن محصول به سبد خرید ابتدا می بایست وارد سایت شوید',
            'confirm_button_text': 'ورود به سایت',
            'icon': 'error'
        })


from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Order


def checkout(request):
    order = Order.objects.filter(
        user=request.user,
        is_paid=False
    ).prefetch_related('orderdetail_set__product').first()

    if not order:
        return redirect('user_basket_page')

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        address = request.POST.get('address', '').strip()
        postal_code = request.POST.get('postal_code', '').strip()
        description = request.POST.get('description', '').strip()

        if not first_name or not last_name or not phone or not address or not postal_code:
            messages.error(request, 'لطفاً اطلاعات ضروری صورتحساب را کامل کنید.')
        else:
            order.first_name = first_name
            order.last_name = last_name
            order.phone = phone
            order.email = email
            order.address = address
            order.postal_code = postal_code
            order.description = description
            order.save()

            messages.success(request, 'اطلاعات صورتحساب با موفقیت ذخیره شد.')

            return redirect('checkout')

    return render(request, 'order/checkout.html', {
        'order': order
    })


@login_required
def payment(request):
    order = Order.objects.filter(
        user=request.user,
        is_paid=False
    ).first()

    if not order:
        return redirect('user_basket_page')

    required_fields = [
        order.first_name,
        order.last_name,
        order.phone,
        order.address,
        order.postal_code,
    ]

    if not all(required_fields):
        messages.error(request, 'لطفاً ابتدا اطلاعات صورتحساب را کامل کنید.')
        return redirect('checkout')

    if not order.orderdetail_set.exists():
        return redirect('user_basket_page')

    return render(request, 'order/payment.html', {
        'order': order
    })