from django.contrib import admin
from cc.models import IssueTracker
from cc.models import MasterCompany
from cc.models import MasterCheckType
from cc.models import MasterIssueType



admin.site.register(IssueTracker)
admin.site.register(MasterCompany)
admin.site.register(MasterCheckType)
admin.site.register(MasterIssueType)
# Register your models here.
