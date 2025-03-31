from django.db import models
from core.basics.models.models import BaseModel
from django.utils.translation import gettext_lazy as _
from .choices import ChoiceFuel, ChoiceTransmission


class Automobile(BaseModel):
    model = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Model'))
    color = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Color'))
    brand = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Brand'))
    engine = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Engine'))
    transmission = models.CharField(
        max_length=100, choices=ChoiceTransmission.choices, default=ChoiceTransmission.MANUAL, 
        verbose_name=_('Transmission')
    )
    fuel_type = models.CharField(
        max_length=50, choices=ChoiceFuel.choices, default=ChoiceFuel.GASOLINE, verbose_name=_('Fuel Type')
    )
    
    num_doors = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Number of doors'))
    num_seats = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Number of seats'))
    year = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Year'))
    
    mileage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_('Mileage (Km)'))
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_('Price (R$)'))
    
    class Meta:
        verbose_name = _('Automobile')
        verbose_name_plural = _('Automobiles')
        db_table = 'automobile'
    
    def __str__(self):
        return f'{self.brand} - {self.model}'
