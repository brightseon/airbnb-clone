from math import ceil
from django.shortcuts import render
from . import models

def all_rooms(request):
    page = request.GET.get('page', 1)
    page = int(page or 1)
    page_size = 10
    print('page_size : ', page_size)
    limit = page_size * page
    print('limit : ', limit)
    offset = limit - page_size
    print('offset : ', offset)
    all_rooms = models.Room.objects.all()[offset:limit]
    print('all_rooms : ', all_rooms)
    page_count = ceil(models.Room.objects.count() / page_size)
    print('page_count : ', page_count)
    print('page_range : ', range(1, page_count))

    return render(request, 'rooms/home.html', {
        'rooms' : all_rooms,
        'page' : page,
        'page_count' : page_count,
        'page_range' : range(1, page_count)
    })