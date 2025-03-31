from django.db import models


class ChoiceFuel(models.TextChoices):
    GASOLINE = "Gasoline", "Gasoline"
    ETHANOL = "Ethanol", "Ethanol"
    DIESEL = "Diesel", "Diesel"
    HYBRID = "Hybrid", "Hybrid"
    ELECTRIC = "Electric", "Electric"
    CNG = "CNG", "Compressed Natural Gas"
    LPG = "LPG", "Liquefied Petroleum Gas"
    BIODIESEL = "Biodiesel", "Biodiesel"


class ChoiceTransmission(models.TextChoices):
    MANUAL = "Manual", "Manual"
    AUTOMATIC = "Automatic", "Automatic"
    SEMI_AUTOMATIC = "Semi-automatic", "Semi-automatic"
    CVT = "CVT", "Continuously Variable Transmission"
    DCT = "DCT", "Dual Clutch Transmission"
    AMT = "AMT", "Automated Manual Transmission"
    DSG = "DSG", "Direct Shift Gearbox"
