from django.db import models
import uuid

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)

    def _str_(self):
        return self.title
    
    @classmethod
    def get_default_id(cls):
        category, created = cls.objects.get_or_create(
            title='default category', 
        )
        return category.id
    
    
class Todo(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    category = models.ForeignKey(
        "core.Category",
        on_delete=models.CASCADE,
        related_name="group",
        null=False,
        default=Category.get_default_id 
    )
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title 

