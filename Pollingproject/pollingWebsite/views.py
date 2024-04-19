from django.shortcuts import render,HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("Hello There Polling website")

    return render(request,'pollswebsite/pollswebsite.html')
