from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
def dis_topic(request):
    topics=Topic.objects.all()
    #topics=Topic.objects.filter(topic_name='urdu')
    topics=Topic.objects.filter(topic_name='kanada')
    d={'topics':topics}
    return render(request,'dis_topic.html',context=d)
def dis_cinema(request):
    cinemas=cinema.objects.all()
    #cinemas=cinema.objects.filter(topic_name='tamil')
    #cinemas=cinema.objects.exclude(topic_name='tamil')
    #cinemas=cinema.objects.all()[0:6]
    #cinemas=cinema.objects.all().order_by('name')
    #cinemas=cinema.objects.all().order_by('-name')
    #cinemas=cinema.objects.all().order_by(Length('name'))
    #cinemas=cinema.objects.all().order_by(Length('name').desc())
    #cinemas=cinema.objects.filter(url__startswith='http')
    #cinemas=cinema.objects.filter(url__endswith='.info/')
    #cinemas=cinema.objects.filter(name__icontains='m')
    #cinemas=cinema.objects.filter(Q(topic_name='english') & Q(name='Randy'))
    #cinemas=cinema.objects.filter(Q(topic_name='english') | Q(name='Ashley'))
    #cinemas=cinema.objects.filter(Q(topic_name='english') | Q(name='Ashley') | Q(url='https://www.kirk-martinez.org/'))
    #cinemas=cinema.objects.filter(name__in=['Jonathan','Randy'])
    #cinemas=cinema.objects.filter(name__regex=r'^[a-zA-Z]{1}h')
    e={'cinemas':cinemas}
    return render(request,'dis_cinema.html',context=e)
def dis_records(request):
    records=acc_record.objects.all()
    #records=acc_record.objects.filter(date__gt='1995-11-11')
    #records=acc_record.objects.filter(date__lt='1995-11-11')
    #records=acc_record.objects.filter(date__year='2011')
    #records=acc_record.objects.filter(date__month='07')
    #records=acc_record.objects.filter(date__day='24')
    ve={'records':records}
    return render(request,'dis_records.html',context=ve)

def update(request):
    cinemas=cinema.objects.all()
    #cinema.objects.filter(topic_name='kanada').update(name='raina',url='http://www.raina.info/',topic_name='bengali')
    #cinema.objects.filter(topic_name='tamil').update(name='jedeja',url='http://www.dhoni.info/')
    e={'cinemas':cinemas}
    return render(request,'dis_cinema.html',context=e)

def update_create(request):
    cinemas=cinema.objects.all()
    t=Topic.objects.get_or_create(topic_name='csk')[0]
    cinema.objects.update_or_create(topic_name='csk',defaults={'topic_name':t,'name':'jedeja','url':'http://www.jadeja.info/'})
    #cinema.objects.update_or_create(topic_name='urdu',defaults={'topic_name':t,'name':'rayudu','url':'http://www.rayudu.info/'})
    e={'cinemas':cinemas}
    return render(request,'dis_cinema.html',context=e)

def delete(request):
    cinemas=cinema.objects.all()
    cinema.objects.filter(topic_name='tamil').delete()
    e={'cinemas':cinemas}
    return render(request,'dis_cinema.html',context=e)



    


    