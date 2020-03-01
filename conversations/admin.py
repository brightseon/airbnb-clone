from django.contrib import admin
from . import models

@admin.register(models.Message)
class MesageAdmin(admin.ModelAdmin) :

    """ Message Admin Definition """

    list_display = ('__str__', 'created')

@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin) :

    """ Conversation Admin Definition """

    list_display = ('__str__', 'count_messages', 'count_participants')