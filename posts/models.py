from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=150)
    likes = models.IntegerField(blank=True,null=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

    # I dont know what is this for
    #def save(self,*args, **kwargs):
        
        #lexer = get_lexer_by_name('python')
        #likes = self.likes and 'table' or False
        #options = self.text and {'title': self.text} or {}
        #formatter = HtmlFormatter(style= 'friendly', likes=likes,
                                  #full=True, **options)
        #self.highlighted = highlight(self.text, lexer, formatter)
        #super(Post, self).save(*args, **kwargs)


    class Meta:
        ordering = ('created','likes')
