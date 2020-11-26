from hashlib import md5

from django.db import models
from django.db.models import Model
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from graphql import GraphQLError


class URLs(models.Model):
    full_url = models.URLField(max_length=300, unique=False)
    url_hash = models.URLField(max_length=300, unique=False)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]

        validate = URLValidator()
        try:
            validate(self.full_url)
        except ValidationError as e:
            raise GraphQLError('invalid url')

        return super().save(*args, **kwargs)

    def get_short_url(self):
        tinyid = short_url.encode_url(self.pk)
        return reverse_lazy('short_url_view', kwargs={'tiny': tinyid})
    def __str__(self):
        return self.full_url


# creating a form
