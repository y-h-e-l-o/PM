from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import *

#Enlever l'annotation pour annuler l'attachement d'image dans summernote
from django_summernote.utils import get_attachment_model 
admin.site.unregister(get_attachment_model())

class SummernoteAdmin(SummernoteModelAdmin):
	summernote_fields = '__all__'

admin.site.site_header = 'Administration Pièces Montées'
admin.site.site_title = 'Pièces Montées'


admin.site.register(Paragraphe, SummernoteAdmin)
admin.site.register(Alerte, SummernoteAdmin)
admin.site.register(Contact, SummernoteAdmin)
admin.site.register(Horaire, SummernoteAdmin)