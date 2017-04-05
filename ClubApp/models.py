from __future__ import unicode_literals

from django.db import models

# Create your models here.

foot = ['Destro','Canhoto']

class team(models.Model):
    name = models.TextField(max_length=60)
    def __str__(self):
        return self.name


class position(models.Model):
    name = models.TextField(max_length=20, verbose_name='Posicao')
    def __str__(self):
        return self.name


class  players(models.Model):
    name = models.TextField(max_length=150)
    age = models.DateField(default=01/01/1900)
    foot = models.TextField(max_length=30)
    #hoto = models.
    role = models.TextField(max_length=50)
    team = models.ForeignKey(team)
    nickname = models.TextField(max_length=60, default='Dodo')
    position = models.ForeignKey(position)
    words = models.TextField(max_length=500, verbose_name='Lema', default='Eu sou o Dougras')
    def __str__(self):
        return self.name




class club_history(models.Model):
    history = models.TextField(max_length=2000)
    def __str__(self):
        return self.history




