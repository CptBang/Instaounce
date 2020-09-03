from django.db import models

class Image(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'images/')
    likes = models.IntegerField(default=0)
    pubDate = models.DateTimeField(auto_now_add=True, editable=False)

    def get_absolute_url(self):
        return reverse('/')
