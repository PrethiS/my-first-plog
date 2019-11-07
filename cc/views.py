from django.db import transaction
from django.db.models import constants
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from cc.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import IssueTrackerserializer
from datetime import datetime
from django.db import connection
import logging
logger = logging.getLogger('cc-logger')

class authentication(IssueTracker):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class board(APIView):
        def get(self, request):
            cursor = connection.cursor()
            cursor.execute("SELECT distinct company_name_id,((count(issue_type_id))*100/3) as value FROM cc_issuetracker where issue_type_id='3' group by company_name_id")
            row = cursor.fetchall()
            rows_affected = cursor.rowcount
            item = 0
            for item in range(rows_affected):
                com_id = row[item][0]
                value = row[item][1]
                m = IssueTracker.objects.filter(company_name_id=com_id)
                for s in range(len(m)):
                    m.update(company_name_id=com_id,
                             availability=value)
            show=IssueTracker.objects.all()
            serializers=IssueTrackerserializer(show, many=True)
            return Response(serializers.data)

        def __init__(self, user=None, **kwargs):
            super().__init__(**kwargs)
            self.user = user
            self.model = IssueTracker
            self.exception_list = list()

        def _user(self, user):
            self.user=user

        def _modelname(self):
            return self.model.__name__

        def _insert(self, company_obj, com_obj, issue_obj, stakeholder_name, user, status):
            m = self.model(
                company_name_id=company_obj.id,
                components_id=com_obj.id,
                issue_type_id=issue_obj.id,
                stakeholder_name=stakeholder_name if stakeholder_name else None,
                created_by=user if user else None,
                status=status if status else None,
                created_on=datetime.now())
            m.full_clean()
            m.save()
            logger.info('DB insertion successful for issue tracker')
            return m

        def _update_data(self, id, company_obj, com_obj, issue_obj, stakeholder_name, comments, status):
            m = self.model.objects.filter(company_name_id=company_obj.id,components_id=com_obj.id)
            print(m)
            m.update(company_name_id=company_obj.id,
                     components_id=com_obj.id,
                     issue_type_id=issue_obj.id,
                     comments=comments if comments else None,
                     stakeholder_name=stakeholder_name if stakeholder_name else None,
                     status=status if status else None,
                     modified_by=self.user,
                     modified_on=datetime.now())
            logger.info('DB Updated successfully for issue tracker details')
            return m

        def find_by_company_and_component_issue_type(self, company_name, components, issue_type):
            m = self.model.objects.filter(company_name__company_name=company_name, components__components=components,
                                          issue_type__issue_type=issue_type).first()
            return m
        def find_by_company_and_component(self, company_name, components):
            m = self.model.objects.filter(company_name__company_name=company_name, components__components=components).first()
            return m

        def _find_by_id(self, id):
            m = self.model.objects.filter(pk=id).first()
            logger.debug('Found entry in DB: %s for component id: %s' % (self._modelname(), id))
            return m

        def _find_by_company_name(self, company_name):
            m = MasterCompany.objects.filter(company_name__iexact=company_name).first()
            logger.debug('Found entry in DB: %s for company_name: %s' % (self._modelname(), company_name))
            return m
        def _find_by_components(self, components):
            m = MasterCheckType.objects.filter(components__iexact=components).first()
            logger.debug('Found entry in DB: %s for components: %s' % (self._modelname(), components))
            return m
        def _find_by_issue_type(self, issue_type):
            m = MasterIssueType.objects.filter(issue_type__iexact=issue_type).first()
            logger.debug('Found entry in DB: %s for issue_type: %s' % (self._modelname(), issue_type))
            return m


        def _update(self, data):
            print(data)
            try:
                with transaction.atomic():
                    id = int(data['id']) if 'id' in data else None
                    company_name = data['company_name']
                    components = data['components']
                    issue_type = data['issue_type']
                    user = data['user'] if 'user' in data else None
                    comments=data['comments'] if 'comments' in data else None
                    stakeholder_name = data['stakeholder_name']
                    status=data['status'] if 'status' in data else None
                    company_obj = self._find_by_company_name(company_name)
                    if not company_obj:
                        raise Exception("company not found in master table")
                    com_obj = self._find_by_components(components)
                    if not com_obj:
                        raise Exception("component not found in master table")
                    issue_obj = self._find_by_issue_type(issue_type)
                    if not issue_obj:
                        raise Exception("issue_type not found in master table")
                    ms_obj = self.find_by_company_and_component_issue_type(company_name, components, issue_type)
                    # if ms_obj:
                    #         raise Exception("duplicate entry error")
                    if id is None:
                        master_obj = self.find_by_company_and_component(company_name,components)
                    else:
                        master_obj = self._find_by_id(id=id) if id else None

                    if not master_obj:
                        self._insert(company_obj, com_obj, issue_obj, stakeholder_name, user, status)
                        logger.debug(
                            'tracker insertion successful in DB: %s' % (self._modelname()))
                    else:
                        self._update_data(id, company_obj, com_obj, issue_obj, stakeholder_name, comments, status)
                        logger.info('Record Updated successfully in DB: %s' % (self._modelname()))


            except Exception as e:
                 self.exception_list.append({constants.ERROR_MSG_STR: str(e)})
            return self.exception_list










#
# def _get_filters(self):
# #         data = Cc().Meta().filters
# #         json_data = JSONRenderer().render(data)
# #         return json_data
# Create your views here.
