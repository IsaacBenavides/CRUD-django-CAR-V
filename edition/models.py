from django.db import models


class Blog(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    author = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog'
