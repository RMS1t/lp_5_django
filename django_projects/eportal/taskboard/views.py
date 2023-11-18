from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import OrderPetition, AdvUser
from .forms import RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import OrderPetition


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

    def get_queryset(self):
        return (
            OrderPetition.objects.filter(user_id=self.request.user).order_by('order_time').reverse()
        )
