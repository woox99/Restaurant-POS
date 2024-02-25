from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Item

# Create your views here.
def index(request):
    pool = []
    for i in range(20):
        random_item = Item.objects.order_by('?').first()
        pool.append(random_item.name)
    serialized_pool = []
    index = 0
    for name in pool:
        serialized_pool.append({
            'name' : name,
            'status' : 'incompleted',
            'index' : index
        })
        index += 1
    request.session['pool'] = serialized_pool
    request.session['index'] = 0
    return redirect('/apps')

def getPool(request):
    pool = request.session['pool']
    return JsonResponse(pool, safe=False)

def toggle(request, name):
    pool = request.session['pool']
    index = request.session['index']
    item = pool[index]
    if(item['name'] == name):
        pool[index]['status'] = 'completed'
        index += 1
        request.session['pool'] = pool
        request.session['index'] = index
        return JsonResponse(item, safe=False)
    return HttpResponse()

# AJAX 
# Saves item to database when pressed if its not already saved
def create(request, name):
    existing_item = Item.objects.filter(name=name).first()
    if existing_item is None:
        Item.objects.create(name = name)
    return HttpResponse()

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
def page2(request):
    return render(request, 'page2.html')
def page1(request):
    return render(request, 'page1.html')
def HH(request):
    return render(request, 'HH.html')
def HH2(request):
    return render(request, 'HH2.html')
def HH3(request):
    return render(request, 'HH3.html')

