from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=200)
    body_text = models.TextField(name='text')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True

    def __str__(self):
        title_text = self.title

        return title_text if len(title_text) < 25 \
            else f"{title_text[:25]}..."


class BlogPost(Post):
    ...
