from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.models import Group

admin.site.register(Userstatus)
admin.site.register(Admincontact)
admin.site.register(Gallery)
admin.site.register(Reachme)
admin.site.register(Eventusers)
admin.site.register(Adminmessagestouser)
admin.site.register(Eventcordinaters)
admin.site.register(Liveupdates)
admin.site.register(Events)
admin.site.register(winners)

admin.site.unregister(Group)

admin.site.site_header = "Project Admin"
admin.site.site_title = "Project Admin."
admin.site.index_title = "Welcome Admin"