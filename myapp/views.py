from django.shortcuts import render
from .models import info
# Create your views here.
def received(request):
    data=info.objects.all()
    for i in data:
      print(i.name,i.department,i.year)
    return render(request,'show.html',{'data':data})