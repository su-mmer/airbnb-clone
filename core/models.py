from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    # core의 model이 db에 등록되는게 아니라 이 model을 사용하는 model이 등록되게 만들어야 함
    # Meta class를 통해 그렇게 만들어주자
    class Meta:
        # abastract는 db에 등록되지 않으며 확장을 위해 사용
        abstract = True
