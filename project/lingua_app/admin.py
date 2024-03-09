from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser
from .models import Meeting 
from django.urls import reverse
from django.utils.html import format_html


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title_of_meeting', 'meeting_link')

    def meeting_link(self, obj):
        url = reverse('meeting', args=[obj.unique_meeting_name])
        return format_html('<a href="{}">View Meeting</a>', url)

admin.site.register(Meeting, MeetingAdmin)

