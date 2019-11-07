from django.db import models
import datetime

from django.db import models
from cc.choices import *
from django.utils import timezone


# only for local
class MasterCompany(models.Model):
    company_name = models.CharField(max_length=200, blank=True, null=True)


class MasterCheckType(models.Model):
    components = models.CharField(max_length=200, blank=True, null=True)


# Masterissuetype example(Harvester issue,etl issue)
class MasterIssueType(models.Model):
    issue_type = models.CharField(max_length=200, blank=True, null=True)

class IssueTracker(models.Model):
    company_name = models.ForeignKey(MasterCompany, null=False, on_delete=models.CASCADE)
    components = models.ForeignKey(MasterCheckType, null=False, on_delete=models.CASCADE)
    issue_type = models.ForeignKey(MasterIssueType, null=True, on_delete=models.CASCADE)
    stakeholder_name = models.CharField(max_length=200, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    status = models.CharField(choices=status_choices, default='null', max_length=200)
    created_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.CharField(max_length=60, blank=True, null=True)
    modified_by = models.CharField(max_length=60, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    availability = models.IntegerField(default=0)
