from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

# import cc
# from cc import models
# from cc.models import IssueTracker


# logger = logging.getLogger("cc-logger")
from cc.views import board


@csrf_exempt
@api_view(['POST'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def push_data(request):
    if request.method == 'POST':
        data = request.data
        user = str(request.user.username)
        user_pass = board()._user(user)
        result =board()._update(data)
        return JsonResponse(result, safe=False)
@csrf_exempt
@api_view(['POST'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def update_schema_data(request):
    if request.method == 'POST':
        posted_data = request.data
        user = str(request.user.username)
        res = board()._update(posted_data)
        return JsonResponse(res, safe=False)