from django.contrib import admin
from . models import Member , Agensi

##DISPLAY LIST ON ADMIN
class MemberAdmin(admin.ModelAdmin):

    list_display = [ 'name', 'membership_plan']

    search_fields = ['name']

admin.site.register(Member,MemberAdmin)

class AgensiAdmin(admin.ModelAdmin):
    
   list_display = [ 'Email', 'agensi_plan']

   search_fields = ['Email']

admin.site.register(Agensi,AgensiAdmin)