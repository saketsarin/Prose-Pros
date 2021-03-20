from django.db import models

class Project(models.Model):
    sceneNum = models.SmallIntegerField()
    character = models.SmallIntegerField()
