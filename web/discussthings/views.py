# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context, RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect
from models import *
import json
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def talk(request, thing_id):
    if not request.POST:
        return
    topic = request.POST.get('topic')
    author = request.POST.get('author')
    thing = Thing.objects.get(pk=thing_id)
    topic = Topic.create(author=author, body=topic, thing=thing)
    return HttpResponse(json.dumps({'success': True, 'body': topic.body}), content_type='application/json')

@csrf_exempt
def reply(request, thing_id, topic_id):
    if not request.POST:
        return
    author = request.POST.get('author')
    body = request.POST.get('body')
    topic = Topic.objects.get(pk=topic_id)
    resp = Response.create(author=author, body=body, topic=topic)
    return HttpResponse(json.dumps({'success': True, 'body': resp.body}), content_type='application/json')