# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.shortcuts import render, get_object_or_404
from models import *


def index(request):
    thing_list = Thing.objects.order_by('name')
    context = Context({
        'thing_list': thing_list,
    })
    return render(request, 'discussthings/index.html', context)


def thing(request, thing_id):
    thing = get_object_or_404(Thing, pk=thing_id)
    return render(request, 'discussthings/thing.html', {'thing': thing})


def thingifier(request, thing_id):
    return HttpResponse('The create/edit thing page - id:%s' % thing_id)


def talk(request, thing_id):
    return HttpResponse('The topic adding thing - id:%s' % thing_id)


def reply(request, thing_id, topic_id):
    return HttpResponse('Replying to topic: %s about thing: %s' % (topic_id, thing_id))