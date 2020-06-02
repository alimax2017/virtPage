from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User
# Create your views here.
def users(request):
    users_list=User.objects.order_by('last_name')
    users_dict={'access_users': users_list}
    #return HttpResponse("<h1>Mar7aba KUKU!</h1>")
    #my_dict={'inserer':"Merci visiter les autres pages egalement"}
    return render(request, 'first_app/users.html', context=users_dict)

def help(request):
    return render(request,'first_app/help.html')

def holidays(request):
    return render(request, 'first_app/holidays.html')

def index(request):
    return render(request, 'first_app/index.html')
