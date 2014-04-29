# -*- encoding: utf8 -*-
from django.db import models


class TodoCategory(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=60)

    class Meta:
        verbose_name_plural = 'Categorias'
        verbose_name = 'Categoria'

    def __unicode__(self):
        return self.name


class Todo(models.Model):

    TODO_CHOICES = (
        (0, 'Não iniciado'),
        (1, 'Em andamento'),
        (2, 'Finalizado')
    )

    name = models.CharField(verbose_name="Nome", max_length=100)
    category = models.ForeignKey(TodoCategory, verbose_name="Categoria", related_name='todos')
    status = models.IntegerField(default=0, choices=TODO_CHOICES)
    obs = models.TextField(verbose_name="Descrição", blank=True)

    class Meta:
        verbose_name_plural = 'Tarefas'
        verbose_name = 'Tarefa'

    def __unicode__(self):
        return self.name

    def is_finished(self):
        return True if self.status == 2 else False

    is_finished.boolean = True
    is_finished.short_description = "Foi concluido?"