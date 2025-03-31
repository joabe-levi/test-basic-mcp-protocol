from django.db import models


class BasicModelManager(models.QuerySet):

    def all(self):
        return self.filter(is_active=True)

    def filter(self, *args, **kwargs):
        kwargs.update({'is_active': True})
        return super().filter(*args, **kwargs)

    def get(self, *args, **kwargs):
        kwargs.update({'is_active': True})
        return super().get(*args, **kwargs)
