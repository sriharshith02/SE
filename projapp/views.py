from django.shortcuts import render
from .models import table
# Create your views here.
r=0
j=0
w=0
c=0
js=0
es=0
pe=0
eq=0
be=0
ie=0
he=0
py=0
def index(request):
    if(request.method=='POST'):
        n=request.POST['name']
        course=request.POST['course']
        t=table.objects.create(name=n,course=course)
        t.save()
        return render(request,"index.html")
    else:
        return render(request,"index.html")
def Registration(request):
    if(request.method=='POST'):
        c=request.POST['stream']
        return render(request,"Registration.html",{'c':c})
def dash(request):
    x=table.objects.all()
    r=0
    j=0
    w=0
    c=0
    js=0
    es=0
    pe=0
    eq=0
    be=0
    ie=0
    he=0
    py=0
    for i in x:
        if(i.course=='Python'):
            py=py+1
        if(i.course=='R and software Development'):
            r=r+1
        if(i.course=='Fundamentals of java programming'):
            j=j+1
        if(i.course=='Web Development or Full Stack Developer'):
            w=w+1
        if(i.course=='Google Cloud Platform Architecture'):
            c=c+1
        if(i.course=='JavaScript'):
            js=js+1
        if(i.course=='Electrical Safety Course'):
            es=es+1
        if(i.course=='Equipment Selection Specialisation'):
            eq=eq+1
        if(i.course=='Plant Earthing course'):
            pe=pe+1
        if(i.course=='Bridge Engineering'):
            be=be+1
        if(i.course=='Irrigation Engineering'):
            ie=ie+1
        if(i.course=='Hydraulic Engineering'):
            he=he+1
    data=[py,r,j,w,c,js,es,eq,pe,be,ie,he]
    label=['Python','R and software Development','Fundamentals of java programming','Web Development or Full Stack Developer',
    'Google Cloud Platform Architecture','JavaScript','Electrical Safety Course','Equipment Selection Specialisation','Plant Earthing course'
    'Bridge Engineering','Irrigation Engineering','Hydraulic Engineering']

    return render(request,"dashboard.html",{'data':data,'label':label})