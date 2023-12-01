from django.urls import path
from taskboard import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.UserCreate.as_view(), name='register'),
    path('my-orders/', views.OrdersByUserListView.as_view(), name='user-orders'),
    path('my-orders/create/', views.OrderCreate.as_view(), name='order-create'),
    path('my-orders/delete/<int:pk>', views.OrderDelete.as_view(), name='order-delete'),
]

urlpatterns += [
    path('staff/orders/', views.OrdersAdminListView.as_view(), name='admin-orders'),
    path('staff/orders/to-end/<int:pk>', views.OrderChangeToEnd.as_view(), name='orders-to-end'),
    path('staff/orders/to-work/<int:pk>', views.OrderChangeToWork.as_view(), name='orders-to-work'),
    path('staff/category/', views.CategoryListView.as_view(), name='category-list'),
    path('staff/category/create/', views.CategoryCreate.as_view(), name='category-create'),
    path('staff/category/delete/<int:pk>', views.CategoryDelete.as_view(), name='category-delete'),

]


