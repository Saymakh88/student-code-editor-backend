from django.db import models

class SavedCode(models.Model):
    title = models.CharField(max_length=255)
    code = models.TextField()
    input_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
