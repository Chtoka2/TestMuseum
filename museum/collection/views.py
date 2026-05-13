from django.shortcuts import render, get_object_or_404
from .models import Exhibit

def exhibit_list(request):
    exhibits = Exhibit.objects.prefetch_related('images').all() # type: ignore
    return render(request, 'collection/index.html', {'exhibits': exhibits})

def exhibit_detail(request, pk):
    exhibit = get_object_or_404(Exhibit.objects.prefetch_related('images'), pk=pk) # type: ignore
    return render(request, 'collection/exhibit.html', {'exhibit': exhibit})