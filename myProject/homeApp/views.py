from django.shortcuts import render
from .models import Users
# Create your views here.
def index(request):
    users = Users.objects.all()
    index=1
    for user in users:
        first=''
        if index % 3 == 1 :
            first='first' 
        else:
            first=''
        index+=1
        setattr(user,'first',first)
    return render(request,'index.html',{'Aluminies':users})
