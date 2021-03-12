from django.shortcuts import render, get_object_or_404
from .models import Anime
from .models import Employee,Product,Anime
from .forms import ProductForm
# Create your views here.


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {'form':form}
#     return render(request,'products/product_create.html', context)

def product_detail_view(request):
    obj = Anime.objects.get(id=1)
    context={"object":obj}
    return render(request, "products/detail.html", context)

def emp_detail_view(request):
    obj = Employee.objects.get(id=1)
    context = {"object":obj}
    return render(request, "products/employee.html", context)


def dynamic_lookup_view(request,id):
    obj = get_object_or_404(Product,id=id)
    context = {'object':obj}
    return render(request, 'products/product_create.html',context)