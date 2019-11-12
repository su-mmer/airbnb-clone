from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """ List model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # 한 명의 유저가 리스트 하나를 만드는 거니까 포링키
    rooms = models.ManyToManyField("rooms.Room", blank=True)
    # 리스트 안에 많은 룸들이 있으니까 매니투매니

    def __str__(self):
        return self.name
