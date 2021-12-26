from enum import Enum
class UnitTypes(Enum):
    """
    Enum for the different unit types.
    """
    VOLUME = 1
    WEIGHT = 2
    TEMPERATURE = 3
    TIME = 4

VolumeUnits = {
    "MILLILITER" : 1.0,
    "LITER" : 1000.0,
    "CUP" : 236.59,
    "PINT" : 568.26125,
    "QUART" : 1136.523,
    "GALLON" : 4546.092,
    "TEASPOON" : 5.0,
    "TABLESPOON": 15.0,
    "TSP" : 5.0,
    "TBSP" : 15.0
}

WeightUnits = {
    "GRAM" : 1.0,
    "G" : 1.0,
    "KILOGRAM" : 1000.0,
    "KG" : 1000.0,
    "POUND" : 453.5,
    "LB" : 453.5,
    "OUNCE" : 28.3495,
    "OZ" : 28.3495
}

TemperatureUnits = {
    "CELSIUS" : 1.0,
    "FARENHEIT" : 2.0,
    "°C" : 1.0,
    "°F" : 2.0
}

TimeUnits = {
    "SECOND" : 1.0,
    "SEC" : 1.0,
    "SEKUNDE": 1.0,
    "MINUTE" : 60.0,
    "MIN" : 60.0,
    "M": 60.0,
    "STUNDE": 3600.0,
    "HOUR" : 3600.0,
    "HR" : 3600.0,
}

def getUnitType(unit: str):
    if unit.upper() in VolumeUnits:
        return UnitTypes.VOLUME
    elif unit.upper() in WeightUnits:
        return UnitTypes.WEIGHT
    elif unit.upper() in TemperatureUnits:
        return UnitTypes.TEMPERATURE
    elif unit.upper() in TimeUnits:
        return UnitTypes.TIME
    else:
        return None

def getUnitConversionFactor(unit: str) -> float:
    if unit.upper() in VolumeUnits:
        return VolumeUnits[unit.upper()]
    elif unit.upper() in WeightUnits:
        return WeightUnits[unit.upper()]
    elif unit.upper() in TemperatureUnits:
        return TemperatureUnits[unit.upper()]
    elif unit.upper() in TimeUnits:
        return TimeUnits[unit.upper()]
    else:
        return 1.0

def unitConversion(fromUnit : str, toUnit : str, value: float):
    if getUnitType(fromUnit) == getUnitType(toUnit):
        if(getUnitType(fromUnit) != UnitTypes.TEMPERATURE):
            return value * (getUnitConversionFactor(fromUnit) / getUnitConversionFactor(toUnit))
        else:
            if (getUnitConversionFactor(fromUnit) == 1.0):
                return value * 1.8 + 32
            else:
                return (value - 32) / 1.8
