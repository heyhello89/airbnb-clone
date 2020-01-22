from django.db import models


class TimeStampedModel(models.Model):

    """ This Stamped Model """

    created = models.DateTimeField(auto_now_add=True)   # Model 생성 시 수시로 업데이트
    updated = models.DateTimeField(auto_now=True)       # Model 저장 시 수시로 업데이트

    class Meta:
        # 데이터베이스에 해당 모델이 등록되지 않게 해준다.
        abstract = True
