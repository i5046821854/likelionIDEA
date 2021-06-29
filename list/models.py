from django.db import models

class list(models.Model):
    name = models.CharField(max_length = 200, default="", unique=True)
    share = models.BooleanField(default='true')  
    icon = models.ImageField(upload_to = "blog/", blank = True, null = True)
    author = models.CharField(max_length = 200, default="")

    def __str__(self):  #객체가 호출될 때 실행됨
        return self.name #제목을 title로 띄우기  