
from django.shortcuts import render

# Create your views here.
class home_view():
    def home_view_func(request, *args, **kwargs):
        my_context={"name":"amaan khan",
                    "occupation":"software engineer",
                    "marital_status":"single" ,
                    "list":[1,2,3,4,5,6,7,8,8,9,10]
        }
        return render(request, "home_view.html", my_context) #render arguments-- request ,"name of template", context

class Anime():
    def attackontitan(request, *args,**kwargs):
        return render(request, "aot.html", {})        
    def codegeass(request, *args,**kwargs):
        return render(request, "codegeass.html", {})

