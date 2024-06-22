from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,null=True, blank = True)  # this foreign key represents that whenever the user does not use this application then delet thier posts also automaticlly
    date_created = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ('-date_created',)

    def comments(self):
        return self.comment_set.all()
    
    def comment_count(self):
        return self.comment_set.all().count()
    
    def __str__(self):
        return self.title 

    


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)

    def __str__(self):
        return self.content