from django.core.paginator import Paginator
from django.shortcuts import render
from . import models

def states_view(request):
    # Filtr parametrlari
    states_filter = request.GET.get('states_filter')  # Kontinent filtri
    search_query = request.GET.get('search_query')  # Qidiruv so‘rovi

    # Asosiy queryset
    queryset = models.State.objects.all().order_by('-uuid')

    # Kontinent bo‘yicha filtrlash
    if states_filter:
        queryset = queryset.filter(continent=states_filter)

    # Qidiruv bo‘yicha filtrlash
    if search_query:
        queryset = queryset.filter(title__icontains=search_query)

    # Filtr ro'yxatini yaratish
    continents = [
        {"value": "", "name": "All", "selected": not states_filter},
        {"value": "Afrika", "name": "Afrika", "selected": states_filter == "Afrika"},
        {"value": "Amerika", "name": "Amerika", "selected": states_filter == "Amerika"},
        {"value": "Asia", "name": "Asia", "selected": states_filter == "Asia"},
        {"value": "Europa", "name": "Europa", "selected": states_filter == "Europa"},
        {"value": "Oceania", "name": "Oceania", "selected": states_filter == "Oceania"},
    ]

    # Paginatsiya
    paginator = Paginator(queryset, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Kontekst
    context = {
        'paginatsa': page_obj,
        'continents': continents,  # Filtr ro'yxatini yuborish
        'search_query': search_query,  # Qidiruv so'rovini yuborish
    }
    return render(request, 'states.html', context)

def state_detail_view(request, uuid):
    state_query = models.State.objects.get(uuid=uuid)
    
    context = {
        'state_query':state_query,
        
    }
    return render(request, 'state_detail.html', context)



def region_detail_view(request, uuid):
    queryset = models.Region.objects.get(uuid=uuid)
    context = {
        'regions':queryset,
    }
    return render(request, 'region_detail.html', context)


def district_detail_view(request, uuid):
    queryset = models.District.objects.get(uuid=uuid)

    context = {
        'districts':queryset
    }
    return render(request, 'district_detail.html', context)

def mfy_detail_view(request, uuid):
    queryset = models.MFY.objects.get(uuid=uuid)

    context = {
        'mfys':queryset
    }
    return render(request, 'mfy_detail.html', context)


def neighborhood_detail_view(request, uuid):
    queryset = models.Neighborhood.objects.get(uuid=uuid)

    context = {
        'neighborhoods':queryset
    }
    return render(request, 'neighborhood_detail.html', context)


def house_detail_view(request, uuid):
    queryset = models.House.objects.get(uuid=uuid)

    context = {
        'houses':queryset
    }
    return render(request, 'house_detail.html', context)


def human_detail_view(request, uuid):
    queryset = models.Human.objects.get(uuid=uuid)

    context = {
        'humans':queryset
    }
    return render(request, 'human_detail.html', context)

