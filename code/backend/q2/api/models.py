from django.db import models
import uuid

class Link(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)

    target = models.URLField()
    created_at = models.DateTimeField(auto_new_add = True)
    last_modified_at = models.DateTimeField(auto_new = True)
