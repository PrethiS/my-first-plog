import rest_framework.fields
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers, fields
from cc.models import *

class IssueTrackerserializer(serializers.ModelSerializer):
    # company_name = rest_framework.fields.CharField(source='company_name.company_name')
    # components = rest_framework.fields.CharField(source='components.components')
    # issue_type= rest_framework.fields.CharField(source='issue_type.issue_type')
    company_name=rest_framework.fields.SerializerMethodField()
    components=rest_framework.fields.SerializerMethodField()
    issue_type=rest_framework.fields.SerializerMethodField()
    #stakeholder_name=rest_framework.SerializerMethodField()
    status=rest_framework.fields.SerializerMethodField()

    def get_company_name(self, value):
        return value.company_name.company_name if value.company_name else value.company_name
    def get_components(self, value):
        return value.components.components if value.components else value.components
    def get_issue_type(self, value):
        return value.issue_type.issue_type if value.issue_type else value.issue_type
    def get_status(self,value):
        return value.status if value.status else value.status

    class Meta:
        model=IssueTracker
        filters={
            'company_name':'company_name__company_name',
            'components':'components__components',
            'issue_type':'issue_type__issue_type',
            'stakeholder_name':'stakeholder_name',
            'comments':'comments',
            'modified_by':'modified_by',
            'availability':'availability'
        }
        fields = ('id', 'company_name', 'components', 'issue_type','stakeholder_name', 'comments', 'modified_by', 'availability', 'status')
        # fields=('company','Components')

