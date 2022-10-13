from django.db import models

class Documents(models.Model):
    title = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title