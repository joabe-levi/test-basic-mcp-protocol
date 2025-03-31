from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _

from core.basics.models.choices import ChoiceOrigin
from core.basics.models.managers import BasicModelManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    
    origin = models.CharField(
        max_length=20, choices=ChoiceOrigin.choices, default=ChoiceOrigin.MANUAL, verbose_name=_('Origin')
    )
    
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    history = HistoricalRecords(inherit=True, verbose_name=_('History'))
    
    objects = BasicModelManager.as_manager()

    class Meta:
        abstract = True
        ordering = ['-created_at']
