from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.chart, name="chart"),
    path("today_total/", views.total1, name="today_total"),
    path("test2/", views.test2, name="test2"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
