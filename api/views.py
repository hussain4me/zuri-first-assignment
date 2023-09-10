from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view()
def get_detail(request, slack_name, track_name):

    detail = { 
                "slack_name": slack_name,
                "current_days": "Monday",
                "utc_time": "2023-09-21T15:04:05Z",
                "track": track_name,
                "github_file_url": "https://github.com/hussain4me/zu-test-assignment/ext",
                "github_repo_url": "https://github.com/hussain4me/zuri-test-assignment/repo",
                "status_code": 200
                
         }

    return Response(detail)
