from django.shortcuts import render, get_object_or_404
from .models import PostVideo

def index(request):
    return render(request, 'main/index.html')

def works(request):
    return render(request, 'main/works.html')


def video_detail(request, video_id):
    video = get_object_or_404(PostVideo, id=video_id)
    return render(request, 'blog/video_detail.html', {
        'video': video
    })
