from django.db import models

class Documents(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title