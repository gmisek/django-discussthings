from django.contrib import admin
from models import Thing
from models import Topic
from models import Response


class TopicInline(admin.TabularInline):
    model = Topic


class ResponseInline(admin.TabularInline):
    model = Response
    list_display = ('date_created', 'author', 'body')


class TopicAdmin(admin.ModelAdmin):
    inlines = [ResponseInline]
    list_display = ('date_created', 'author', 'body')


class ThingAdmin(admin.ModelAdmin):
    inlines = [TopicInline]


admin.site.register(Thing, ThingAdmin)
admin.site.register(Topic, TopicAdmin)
#admin.site.register(Response)
