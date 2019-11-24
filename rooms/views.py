from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10  # 10개씩 한 페이지
    paginate_orphans = 5  # 고아 5개는 앞으로 땡김
    ordering = "created"  # created 순으로 정렬
    context_object_name = "rooms"  # html에서 쓸 context명


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()
