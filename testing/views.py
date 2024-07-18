from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'testing/index.html')#seharusnya views tidak usah urus html yang urus adalah template
