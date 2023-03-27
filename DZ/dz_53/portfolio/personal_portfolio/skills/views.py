from django.shortcuts import render, get_object_or_404
from .models import Skills


def index(request):
    projects = Skills.objects.all()
    return render(request, 'skills/index.html', {'projects': projects})


# def work_all(request):
#     projects = Skills.objects.all()
#     return render(request, 'skills/work_all.html', {'projects': projects})


# def work(request, work_id):
#     work = get_object_or_404(Skills, pk=work_id)
#     context = {'work': work}
#     return render(request, 'skills/work.html', context)
