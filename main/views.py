from django.shortcuts import render

from main.forms import FormToValidate
from main.models import Category, Service


# def validator(request):
#     form = FormToValidate()
#     if request.method=='POST':
#         form = FormToValidate(request.POST)
#         context = {'form': form}
#         if form.is_valid():
#             return render(request, 'validation.html', context)
#     context = {'form': form}
#     return render(request, 'validation.html', context)


def get_category(request):
    category_of_manic = Category.objects.get(title__startswith="Па")
    if category_of_manic:
        print(category_of_manic.title)
    services_of_manic = category_of_manic.services.all()
    for service in services_of_manic:
        print(service.title,service.price)
    context = {"category":category_of_manic}
    return render(request,'category.html',context)

def get_service(request,slug):
    service_po_category = Service.objects.filter(category__slug=slug)
    context = {"service_po_category":service_po_category}
    return render(request,"service.html",context)
