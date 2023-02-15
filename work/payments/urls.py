from django.urls import path
from django.views.decorators.cache import cache_page
from . import views


urlpatterns = [
    path('item/<int:item_id>/', views.item_detail, name='item'),
    path('config/', views.stripe_config),
    path('buy/<int:id>', views.create_checkout_session, name='buy'),

    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),

]
