from django.conf.urls import include, url
from django.contrib import admin
from cc.models import IssueTracker
from cc import views
from django.conf.urls import include, url
from cc.models import IssueTracker
from cc import views
from cc import view_controller

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^IssueTracker/', views.board.as_view()),
    url(r'push_data', view_controller.push_data, name='push_data'),
    url(r'iris1_update_template_data', view_controller.update_schema_data, name='update_schema_data'),
]