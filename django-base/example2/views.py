from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world from Example 2!")
