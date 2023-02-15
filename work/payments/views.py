from django.shortcuts import render, get_object_or_404
from .models import Item
from django.conf import settings # new
from django.http.response import JsonResponse # new
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic.base import TemplateView


stripe.api_key = settings.STRIPE_SECRET_KEY


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    # Здесь код запроса к модели и создание словаря контекста
    context = {
        'item': item,
    }
    return render(request, 'home.html', context)

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request, id):
    if request.method == 'GET':
        item = get_object_or_404(Item, id=id)
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                        'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': item.price*100  ,
                    },
                    'quantity': 1,
                    }],
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'