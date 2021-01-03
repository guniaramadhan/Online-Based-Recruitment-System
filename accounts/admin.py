from django.contrib import admin
from .models import Educ,Applicant,Gstudent,Application,User

admin.site.register(Educ)
admin.site.register(User)
admin.site.register(Applicant)
admin.site.register(Gstudent)
admin.site.register(Application)

# Register your models here.
