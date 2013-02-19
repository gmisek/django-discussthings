# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from models import *


def index(request):
    thing_list = Thing.objects.order_by('name')
    template = loader.get_template('discussthings/index.html')
    context = Context({
        'thing_list': thing_list,
    })
    return HttpResponse(template.render(context))


def thing(request, thing_id):
    return HttpResponse('Thing page - id: %s' % thing_id)


def thingifier(request, thing_id):
    return HttpResponse('The create/edit thing page - id:%s' % thing_id)


def talk(request, thing_id):
    return HttpResponse('The topic adding thing - id:%s' % thing_id)


def reply(request, thing_id, topic_id):
    return HttpResponse('Replying to topic: %s about thing: %s' % (topic_id, thing_id))