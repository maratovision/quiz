from django.contrib import admin
from .models import *
# Register your models here.

class PollAdmin(admin.ModelAdmin):
    list_display = ['name', 'points', 'date']


admin.site.register(Poll, PollAdmin)
admin.site.register(Questions)
admin.site.register(ChoiceAnswer)
admin.site.register(Answer)