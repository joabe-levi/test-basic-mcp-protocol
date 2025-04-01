from django.db import models


class ChoiceOrigin(models.TextChoices):
    MANUAL = 'Manual', 'Manual'
    IMPORTED = 'Import', 'Import'
    SYSTEM = 'System', 'System'
    INTEGRATION = 'Integration', 'Integration'
