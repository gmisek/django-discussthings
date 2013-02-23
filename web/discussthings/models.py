from django.db import models
from django.forms import ModelForm
import time

class Thing(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="discussthings/static/thing_pictures/", null=True)

    def __unicode__(self):
        return self.name

class ThingForm(ModelForm):
    class Meta:
        model = Thing

class Topic(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    thing = models.ForeignKey(Thing, default=1)

    @classmethod
    def create(cls, author, body, thing):
        topic = cls(author=author,  body=body, thing=thing)
        topic.save()
        return topic

    def __unicode__(self):
        return time.strftime("%m-%d-%Y %H:%M:%S") + ' ' + str(self.body)[:100]


class Response(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    topic = models.ForeignKey(Topic, default=1)
    parent = models.ForeignKey('self', null=True)

    @classmethod
    def create(cls, author, body, topic):
        resp = cls(author=author, body=body, topic=topic)
        resp.save()
        return resp

    def __unicode__(self):
        return time.strftime("%m-%d-%Y %H:%M:%S") + ' ' + str(self.body)[:100]