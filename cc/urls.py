from cc import view_controller
from django.conf.urls import include, url
from cc import views

urlpatterns = [
        url(r'push_data', view_controller.push_data, name='push_data'),
        url(r'iris1_update_template_data', view_controller.update_schema_data, name='update_schema_data'),
        url(r'IssueTracker', views.board.as_view()),
]