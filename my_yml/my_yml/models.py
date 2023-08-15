from django.db import models
from datetime import datetime


class Chart(models.Model):
    chart_date = models.DateTimeField("차트 날짜", default=datetime.now)
    rank = models.IntegerField("노래 순위")
    title = models.CharField("노래 제목", max_length=100)
    artist = models.CharField("가수", max_length=100)
    album_image = models.TextField("앨범 이미지", max_length=100)

    def __str__(self):
        return f"{self.rank}. {self.title} - {self.artist}"


class BillboardChart(models.Model):
    chart_date = models.DateTimeField("차트 날짜", default=datetime.now)
    rank = models.IntegerField("노래 순위")
    title = models.CharField("노래 제목", max_length=100)
    artist = models.CharField("가수", max_length=100)
    album_image = models.TextField("앨범 이미지", max_length=100)

    def __str__(self):
        return f"{self.rank}. {self.title} - {self.artist}"


class JpopChart(models.Model):
    chart_date = models.DateTimeField("차트 날짜", default=datetime.now)
    rank = models.IntegerField("노래 순위")
    title = models.CharField("노래 제목", max_length=100)
    artist = models.CharField("가수", max_length=100)
    album_image = models.TextField("앨범 이미지", max_length=100)

    def __str__(self):
        return f"{self.rank}. {self.title} - {self.artist}"
