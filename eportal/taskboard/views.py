from audioop import reverse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .models import OrderPetition, AdvUser, Category
from .forms import RegisterForm, OrderForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect


def index(request):
    orders = OrderPetition.objects.filter(status__exact="E").order_by('order_time').reverse()[:4]
    in_working = OrderPetition.objects.filter(status__exact="W").count()
    context = {
        'orders': orders,
        'in_working': in_working,
    }
    return render(request, 'index.html', context=context)


class UserCreate(CreateView):
    # Модель куда выполняется сохранениеs
    model = AdvUser
    # Класс на основе которого будет валидация полей
    form_class = RegisterForm

    template_name = 'registration/user_create.html'

    success_url = '/accounts/login/'


class OrdersByUserListView(LoginRequiredMixin, ListView):
    model = OrderPetition
    template_name = 'orders/user_orders.html'
    paginate_by = 10
    context_object_name = 'order_list'

    def get_queryset(self):
        return (
            OrderPetition.objects.filter(user_id=self.request.user).order_by('order_time').reverse()
        )


class OrderDelete(LoginRequiredMixin, DeleteView):
    model = OrderPetition
    success_url = '/my-orders/'
    template_name = 'order_delete_form.html'

    def form_valid(self, form):
        try:
            if self.object.user_id == self.request.user:
                self.object.delete()
                return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("order-delete", kwargs={"pk": self.object.pk})
            )


class OrderCreate(LoginRequiredMixin, CreateView):
    model = OrderPetition
    form_class = OrderForm
    template_name = 'orders/order_create.html'
    success_url = '/my-orders/'
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


class OrdersAdminListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = OrderPetition
    template_name = 'admin/admin_orders.html'
    permission_required = 'is_staff'
    paginate_by = 10
    context_object_name = 'order_list'
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"


class OrderChangeToWork(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = OrderPetition
    permission_required = 'is_staff'
    fields = ['comment']
    template_name = 'admin/order_in_working_form.html'
    success_url = '/staff/orders/'
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"

    def form_valid(self, form):
        form.instance.status = 'W'
        return super().form_valid(form)


class OrderChangeToEnd(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = OrderPetition
    template_name = 'admin/order_end_form.html'
    permission_required = 'is_staff'
    fields = ['design_image']
    success_url = '/staff/orders/'
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"

    def form_valid(self, form):
        form.instance.status = 'E'
        return super().form_valid(form)


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    template_name = 'admin/category_list.html'
    permission_required = 'is_staff'
    paginate_by = 10
    context_object_name = 'category_list'
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"


class CategoryCreate(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Category
    permission_required = 'is_staff'
    fields = ['name']
    template_name = 'admin/category_create.html'
    success_url = '/staff/category/'
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"


class CategoryDelete(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Category
    permission_required = 'is_staff'
    template_name = 'admin/category_delete.html'
    success_url = '/staff/category/'
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"
