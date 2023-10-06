from django.shortcuts import render

def index_view(request):
    return render(request,'index.html')

def provider_view(request):
    return render(request,'provider.html')

def customer_view(request):
    return render(request, 'customer.html')

def policy_view(request):
    return render(request, 'policy.html')

def payment_view(request):
    return render(request,'payment.html')