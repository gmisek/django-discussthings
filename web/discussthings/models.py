from django.db import models
import time

# Create your models here.


class Thing(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="discussthings/static/thing_pictures/", null=True)

    def __unicode__(self):
        return self.name


class Topic(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    thing_id = models.ForeignKey(Thing, default=1)

    def __unicode__(self):
        return time.strftime("%m-%d-%Y %H:%M:%S") + ' ' + str(self.body)[:100]


class Response(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    topic_id = models.ForeignKey(Topic)
    parent_id = models.ForeignKey('self', null=True)

    def __unicode__(self):
        return time.strftime("%m-%d-%Y %H:%M:%S") + ' ' + str(self.body)[:100]