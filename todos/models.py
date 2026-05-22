from datetime import date

from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de Vencimento", null=False, blank=False, default=date.today)
    finished_at = models.DateField(verbose_name="Concluído em", null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['deadline']

    def mark_has_finished(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()