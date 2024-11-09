from django.shortcuts import render

from video.models import Video


# Create your views here.
def homepage(request):
    breaking_video = Video.objects.all().order_by('-id')
    context = {
        'breaking_video': breaking_video
    }
    return render(request, 'index.html', context)
