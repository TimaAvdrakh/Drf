from django.db import models

# Create your models here.

def upload_status_image(instance, filename):
    return ""


class Status(models.Model):
    user = models.ForeignKey()
    content = models.TestField(null = True, blank = True)
    image = models.ImageField(upload_to = upload_status_image, null = True, blank = True)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.content)[:50]
