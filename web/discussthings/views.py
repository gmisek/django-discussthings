# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context, RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect
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


def thingifier(request):
    if request.method == 'POST':
        form = ThingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/things/')
    else:
        form = ThingForm()
    return render_to_response('discussthings/thingifier.html',
        {'form': form},
        context_instance = RequestContext(request)
    )


def talk(request, thing_id):
    return HttpResponse('The topic adding thing - id:%s' % thing_id)


def reply(request, thing_id, topic_id):
    return HttpResponse('Replying to topic: %s about thing: %s' % (topic_id, thing_id))