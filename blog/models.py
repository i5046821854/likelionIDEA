from django.db import models

# Create your models here.
class blog(models.Model): #id에 대한 column 안써도됨 
    lat = models.FloatField(max_length=50, default='0')
    lng = models.FloatField(max_length=50, default='0')
    title = models.CharField(max_length = 200)
    writer = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    body = models.TextField()
   # image = models.ImageField(upload_to = "blog/", blank = True, null = True)
    image = models.ImageField(upload_to = "blog/", blank = True, null = True)
    
    def __str__(self):  #객체가 호출될 때 실행됨
        return self.title #제목을 title로 띄우기  

    def summary(self): #본문 간단히 나타내기
        return self.body[:100]