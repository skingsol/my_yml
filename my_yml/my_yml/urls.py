from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.chart, name="chart"),
    path("today_total/", views.total1, name="today_total"),
    path("billboard_total/", views.billboard_total1, name="billboard_total"),
    path("jpop_total/", views.jpop_total1, name="jpop_total"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
