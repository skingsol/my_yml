import os
import requests
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect, get_object_or_404
from .models import Chart, BillboardChart, JpopChart
from .crawling import get_chart, get_billboard_chart, get_jpop_chart


def chart(request):
    # 기존 DB의 차트 데이터 제거하기
    # Chart.objects.all().delete()
    # BillboardChart.objects.all().delete()
    # JpopChart.objects.all().delete()

    # 새로운 차트 가져오기
    # chart_list = get_chart()
    # billboard_chart_list = get_billboard_chart()
    # jpop_chart_list = get_jpop_chart()

    # 차트 10개만 메인에 보여주기
    top_5_chart = Chart.objects.all()[:5]
    top_10_chart = Chart.objects.all()[5:10]

    billboard_top_5_chart = BillboardChart.objects.all()[:5]
    billboard_top_10_chart = BillboardChart.objects.all()[5:10]

    jpop_top_5_chart = JpopChart.objects.all()[:5]
    jpop_top_10_chart = JpopChart.objects.all()[5:10]

    context = {
        "chart_list1": top_5_chart,
        "chart_list2": top_10_chart,
        "billboard_chart_list1": billboard_top_5_chart,
        "billboard_chart_list2": billboard_top_10_chart,
        "jpop_chart_list1": jpop_top_5_chart,
        "jpop_chart_list2": jpop_top_10_chart,
    }

    return render(request, "my_yml/chart.html", context)


# 오늘 탑100 전체 보여주기
def total1(request):
    top_100_chart = Chart.objects.all()[:100]

    context = {
        "chart_list1": top_100_chart,
    }

    return render(request, "my_yml/today_total.html", context)


# 빌보드 탑100 전체 보여주기
def billboard_total1(request):
    top_100_chart = BillboardChart.objects.all()[:100]

    context = {
        "billboard_chart_list1": top_100_chart,
    }

    return render(request, "my_yml/billboard_total.html", context)


# J-POP 탑100 전체 보여주기
def jpop_total1(request):
    top_100_chart = JpopChart.objects.all()[:100]

    context = {
        "jpop_chart_list1": top_100_chart,
    }

    return render(request, "my_yml/jpop_total.html", context)
