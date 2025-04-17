from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Glacier

def home(request):
    return render(request, 'home.html')

def glacier_list(request):
    # Get all glaciers ordered by creation date in descending order (newest first)
    glaciers = Glacier.objects.all().order_by('-created_at')
    
    # Create paginator with exactly 10 items per page
    paginator = Paginator(glaciers, 9)
    
    # Get the current page number from the request
    page_number = request.GET.get('page', 1)
    
    # Get the page object
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'glacier_list.html', {
        'page_obj': page_obj,
        'glaciers': page_obj.object_list
    })

def glacier_detail(request, pk):
    glacier = get_object_or_404(Glacier, pk=pk)
    return render(request, 'glacier_detail.html', {'glacier': glacier}) 