from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Topic(MPTTModel):
    type_topic = (
        (1,'Легкий'),
        (2,'Средний'),
        (3,'Сложный'),
    )
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    type = models.IntegerField(choices=type_topic)
    count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}[type={self.type},count={self.count}]'

