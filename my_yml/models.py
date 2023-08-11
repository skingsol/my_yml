from django.db import models


# class My_yml(models.Model):
#     """
#     차트항목
#     순위
#     앨범이미지
#     제목
#     가수
#     """
# chart_name = models.CharField(max_length=50)
# rank = models.int
# title = models.CharField(max_length=50)
# DateTimeField 옵션
# auto_now_add : 처음 입력시 날짜/시간으로 셋팅 (insert시에만)
# # auto_now : 수정할때마다 계속 시간과 날짜가 자동 업데이트 (update시에만)
# created = models.DateTimeField(auto_now_add=True)
# complete = models.BooleanField(default=False)
# important = models.BooleanField(default=False)
# description = models.TextField()
