import os
import requests
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect, get_object_or_404
from .models import Chart
from .crawling import get_chart


def chart(request):
    # 기존 DB의 차트 데이터 제거하기
    # Chart.objects.all().delete()

    # 새로운 차트 가져오기
    # chart_list = get_chart()

    # 차트 10개만 메인에 보여주기
    top_5_chart = Chart.objects.all()[:5]
    top_10_chart = Chart.objects.all()[5:10]

    context = {
        "chart_list1": top_5_chart,
        "chart_list2": top_10_chart,
    }

    return render(request, "my_yml/chart.html", context)


def total1(request):
    top_100_chart = Chart.objects.all()[:100]

    context = {
        "chart_list1": top_100_chart,
    }

    return render(request, "my_yml/today_total.html", context)


def test2(request):
    return render(request, "my_yml/test2.html")
