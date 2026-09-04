from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import  ListView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from order.models import Order, OrderDetail
from product.models import Product
from .forms import ChangePasswordForm
from .models import UserFavorite


# Create your views here.




class ChangePasswordView(LoginRequiredMixin, FormView):

    template_name = 'user_panel/change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('home')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['user'] = self.request.user

        return kwargs


    def form_valid(self, form):

        user = self.request.user

        user.set_password(
            form.cleaned_data['password']
        )

        user.save()

        #کاربر بعد از تغییر رمز بیرون نمیپره و سشن اپدیت میشه
        update_session_auth_hash(
            self.request,
            user
        )


        return super().form_valid(form)




@login_required
def user_basket(request: HttpRequest):

    current_order, created = Order.objects.prefetch_related('orderdetail_set__product').get_or_create(is_paid=False,user=request.user)

    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount,

    }

    return render(request,'user_panel/user_basket.html',context)



@login_required
def remove_order_detail(request):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })

    deleted_count, deleted_dict = OrderDetail.objects.filter(id=detail_id, order__is_paid=False, order__user_id=request.user.id).delete()

    if deleted_count == 0:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel/user_basket_content.html', context)
    })



@login_required
def change_order_detail_count(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')
    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_or_state'
        })

    order_detail = OrderDetail.objects.filter(id=detail_id, order__user_id=request.user.id, order__is_paid=False).first()

    if order_detail is None:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    if state == 'increase':
        order_detail.count += 1
        order_detail.save()
    elif state == 'decrease':
        if order_detail.count == 1:
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else:
        return JsonResponse({
            'status': 'state_invalid'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel/user_basket_content.html', context)
    })



class UserFavoritesView(ListView):
    template_name = 'user_panel/user_favorites.html'
    model = UserFavorite
    context_object_name = 'favorites'
    paginate_by = 9

    def get_queryset(self):
        return UserFavorite.objects.filter(user=self.request.user).select_related('product').prefetch_related('product__images').order_by('-id')



@login_required
def toggle_favorite(request):

    product_id = request.GET.get('product_id')

    if not product_id:
        return JsonResponse({
            'status': 'error',
            'message': 'محصول مشخص نشده است.'
        }, status=400)

    product = Product.objects.filter(
        id=product_id,
        is_active=True,
        is_deleted=False
    ).first()

    if product is None:
        return JsonResponse({
            'status': 'error',
            'message': 'محصول مورد نظر یافت نشد.'
        }, status=404)

    favorite = UserFavorite.objects.filter(
        user=request.user,
        product=product
    ).first()

    if favorite:

        favorite.delete()

        return JsonResponse({
            'status': 'success',
            'is_favorite': False,
            'message': 'این محصول از لیست علاقه‌مندی‌های شما حذف شد.',
            'icon': 'info'
        })

    UserFavorite.objects.create(
        user=request.user,
        product=product
    )

    return JsonResponse({
        'status': 'success',
        'is_favorite': True,
        'message': 'محصول با موفقیت به لیست علاقه‌مندی‌های شما اضافه شد.',
        'icon': 'success'
    })


@login_required
def tracking(request):
    order = None

    if request.method == 'POST':
        tracking_code = request.POST.get('order', '').strip()
        email = request.POST.get('email', '').strip()

        order = Order.objects.filter(
            tracking_code=tracking_code,
            user=request.user,
            is_paid=True
        ).prefetch_related('orderdetail_set__product').first()

        if order:
            if order.email and order.email != email:
                order = None

        if not order:
            messages.error(request, 'سفارشی با اطلاعات وارد شده پیدا نشد.')

    return render(request, 'user_panel/tracking.html', {
        'order': order
    })




@login_required
def user_panel(request):
    user = request.user

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', '').strip()
        user.last_name = request.POST.get('last_name', '').strip()
        user.email = request.POST.get('email', '').strip()
        user.about_user = request.POST.get('about_user', '').strip()
        user.address = request.POST.get('address', '').strip()

        avatar = request.FILES.get('avatar')

        if avatar:
            user.avatar = avatar

        user.save()

        messages.success(request, 'اطلاعات شما با موفقیت ذخیره شد.')

    return render(request, 'user_panel/user_panel.html', {
        'user': user
    })