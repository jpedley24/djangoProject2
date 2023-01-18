from django.shortcuts import render
from myapp import support_functions
from myapp.models import Currency


# Create your views here.

def home(request):
    data = dict()
    import datetime
    data["time"] =datetime.date.today()
    return render(request, "home.html", context=data)

def maintenance(request):
    data = dict()
    choice = "NONE"
    try:
       choice = request.GET["selection"]
       if choice == "currencies":
           support_functions.add_currencies(support_functions.get_currency_list())
       c_list = Currency.objects.all()
       #print("Got c_list", len(c_list))
       data['currencies'] = c_list
       #return HttpResponseRedirect(reverse('currencies'))

    except:
        pass
    print(choice)

    return render(request,"maintenance.html",context=data)

def view_currencies(request):
    data = dict()
    c_list = Currency.objects.all()
    data['currencies'] = c_list
    return render(request,'currencies.html',context=data)