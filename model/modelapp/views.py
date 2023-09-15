from django.shortcuts import render

from modelapp.models import Person

def crate(request):
    if request.method=='POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        phone = request.POST.get('phone') 
        pi = Person(name=name,city=city,phone=phone)
        pi.save()
    return render(request,'index.html')
    
    