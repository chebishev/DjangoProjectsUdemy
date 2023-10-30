from django.shortcuts import render,get_object_or_404,reverse,redirect
from .models import Product,OrderDetail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponseNotFound
import stripe,json
# Create your views here.
def index(request):
    products = Product.objects.all()
    
    return render(request,'common/index.html',{'products':products})

def detail(request,id):
    product = Product.objects.get(id=id)
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'common/product_details.html',{'product':product,'stripe_publishable_key':stripe_publishable_key})
    
    
@csrf_exempt
def create_checkout_session(request,id):
    print("#body"*20)
    print(request.body)
    request_data = json.loads(request.body)
    product = Product.objects.get(id=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        customer_email = request_data['email'],
        payment_method_types = ['card'],
        line_items=[
            {
                'price_data':{
                    'currency':'usd',
                    'product_data':{
                        'name':product.name,
                    },
                    'unit_amount':int(product.price * 100)
                },
                'quantity':1,
            }
        ],
        mode='payment',
        success_url = request.build_absolute_uri(reverse('success')) +
        "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url = request.build_absolute_uri(reverse('failed')),
        
    )
    
    order = OrderDetail()
    order.customer_email = request_data['email']
    order.product = product
    order.stripe_payment_intent = checkout_session['payment_intent']
    order.amount = int(product.price)
    order.save()
    print("#"*20)
    print(JsonResponse({'sessionId':checkout_session.id}))
    return JsonResponse({'sessionId':checkout_session.id})
    
def payment_success_view(request):
    session_id = request.GET.get('session_id')
    if session_id is None:
        return HttpResponseNotFound()
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.retrieve(session_id)
    order = get_object_or_404(OrderDetail,stripe_payment_intent= session.payment_intent)
    order.has_paid=True
    # updating sales stats for a product
    product = Product.objects.get(id=order.product.id)
    product.total_sales_amount = product.total_sales_amount + int(product.price)
    product.total_sales = product.total_sales + 1
    product.save()
    # updating sales stats for a product
    order.save()
    
    return render(request,'common/payment_success.html',{'order':order})
    
def payment_failed_view(request):
    return render(request,'common/payment_failed.html')
