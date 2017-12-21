from django.shortcuts import render

# Create your views here.



def index(request):

    return render(request,"index.html")


def AddData(request):
    if request.method == "GET":
        return render(request,"adddata.html")
    else:
        user = request.POST.get("user")
        print(user)
        return render(request,"add_response.html",{"user":user})