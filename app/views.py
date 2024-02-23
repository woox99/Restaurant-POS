from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Item

# Create your views here.
def index(request):
    random_items = []
    for i in range(10):
        random_item = Item.objects.order_by('?').first()
        random_items.append(random_item.name)
    request.session['pool'] = random_items
    return redirect('/apps')

def getPool(request):
    pool = request.session['pool']
    serialized_pool = []
    for name in pool:
        serialized_pool.append({
            'name' : name
        })
    print(serialized_pool)
    return JsonResponse(serialized_pool, safe=False)

def apps(request):
    return render(request, 'apps.html')
def apps2(request):
    return render(request, 'apps2.html')
def soups(request):
    return render(request, 'soups.html')
def steaks(request):
    return render(request, 'steaks.html')
def steaks2(request):
    return render(request, 'steaks2.html')
def seafood(request):
    return render(request, 'seafood.html')
def addons(request):
    return render(request, 'addons.html')
def sides(request):
    return render(request, 'sides.html')
def desserts(request):
    return render(request, 'desserts.html')
def desserts2(request):
    return render(request, 'desserts2.html')
def bar(request):
    return render(request, 'bar.html')

def create(request, name):
    existing_item = Item.objects.filter(name=name).first()
    if existing_item is None:
        Item.objects.create(name = name)
    return HttpResponse()