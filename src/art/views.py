from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from content.models import Drawing


def index(request):
    queryset = Drawing.objects.order_by('-timestamp')[0:8]
    if queryset:
        context = {
            'queryset': queryset,
        }
    return render(request, 'index.html', context)


def gallery(request):
    queryset = Drawing.objects.order_by('-timestamp')
    if queryset:
        paginator = Paginator(queryset, 6)
        page_request_var = 'page'
        page = request.GET.get(page_request_var)
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)
        a = paginated_queryset.has_other_pages
        context = {
            'queryset': paginated_queryset,
            'page_request_var': page_request_var,
            'a': a,
        }
    else:
        context = {}
    # if queryset:
    #     context = {
    #         'queryset': queryset,
    #     }
    return render(request, 'gallery.html', context)


def details(request, id):
    drawing = get_object_or_404(Drawing, id=id)
    context = {
        'drawing': drawing,
    }
    return render(request, 'details.html', context)


def post_details(request):
    return render(request, 'post-details.html', {})


def events(request):
    return render(request, 'events.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})
