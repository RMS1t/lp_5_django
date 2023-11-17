from django.shortcuts import render
from django.views.generic import CreateView
from taskboard.models import OrderPetition, RegisterForm, AdvUser


# Create your views here.
def index(request):
    orders = OrderPetition.objects.filter(status__exact="E").order_by('order_time').reverse()[:4]
    in_working = OrderPetition.objects.filter(status__exact="W").count()
    context = {
        'orders': orders,
        'in_working': in_working,
    }

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'index.html', context=context)


class UserCreate(CreateView):
    # Модель куда выполняется сохранениеs
    model = AdvUser
    # Класс на основе которого будет валидация полей
    form_class = RegisterForm

    template_name = 'registration/user_create.html'

    success_url = '/accounts/login/'