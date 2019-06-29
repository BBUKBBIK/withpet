from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    author = models.ForeignKey(User, editable =False, null=True,
    blank=True, on_delete=models.SET_NULL,)
    title=models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]

class Comment(models.Model):
    post_key = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.comment_contents
        