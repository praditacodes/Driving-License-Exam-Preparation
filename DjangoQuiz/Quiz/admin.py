from django.contrib import admin
from .models import *
from .models import QuesModel 
 
# Register your models here.
admin.site.register(QuesModel)
admin.site.register(QuizResult)