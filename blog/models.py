from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

# いいねモデル  
class Ine(models.Model):  
    ip_address = models.CharField('IPアドレス', max_length=20)
    parent = models.ForeignKey(Article, on_delete=models.CASCADE)