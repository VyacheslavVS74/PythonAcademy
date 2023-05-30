from django.shortcuts import render
from .models import CmsSlider


def first_page(request):
    slider_list = CmsSlider.objects.all()
    context = {
        'slider_list': slider_list,
    }
    return render(request, 'cms/index.html', context)
