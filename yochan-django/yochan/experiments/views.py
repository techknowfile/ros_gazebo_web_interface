from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from experiments.models import GazeboVideoStream 

# Create your views here.
def index(request):
    return HttpResponse('Hello World');

def experiment(request, gazebo_title):
    gazebo_video_stream = get_object_or_404(GazeboVideoStream,
            title=gazebo_title)
   
    return render(request, 'experiments/experiment.html',
            {'gazebo_video_stream': gazebo_video_stream })
