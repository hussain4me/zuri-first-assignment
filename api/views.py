from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime


# Create your views here.
@api_view()
def get_detail(request):

    slack_name = request.GET.get('slack_name', None)

    track_name = request.GET.get('track_name', None)

    current_date = datetime.date.today()


    
    # Get the current UTC time
    current_utc_time = datetime.datetime.utcnow()

    # Define a time range of +/- 2 hours
    time_range = datetime.timedelta(hours=2)

    # Calculate the minimum and maximum allowed times
    min_time = current_utc_time - time_range
    max_time = current_utc_time + time_range

    # Get the current UTC time as a string
    min_time_str = min_time.strftime('%Y-%m-%d %H:%M:%S')
    max_time_str = max_time.strftime('%Y-%m-%d %H:%M:%S')

# Get the name of the day of the week
    day_of_week = current_date.strftime('%A')

    detail = { 
                "slack_name": slack_name,
                "current_days": day_of_week,
                "utc_time": "Min. =>"+ min_time_str + "  - Man =>" + max_time_str,
                "track": track_name,
                "github_file_url": "https://github.com/hussain4me/zu-test-assignment/ext",
                "github_repo_url": "https://github.com/hussain4me/zuri-first-assignment",
                "status_code": 200
         }

    return Response(detail)
