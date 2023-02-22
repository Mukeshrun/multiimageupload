from django.shortcuts import render
from . models import Image
def index(request):
    if request.method=='POST':
        images=request.FILES.getlist('files')
        for img in images:
            Image.objects.create(image=img)
    data=Image.objects.all()
    return render(request,'multiple/index.html',{'key':data})
