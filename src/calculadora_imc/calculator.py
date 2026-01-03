"""
Core BMI calculation and classification logic.
"""


def calcular_imc(peso: float, altura: float) -> float:
    """
    Calculate BMI (Body Mass Index).
    
    Args:
        peso: Weight in kilograms
        altura: Height in meters
        
    Returns:
        BMI value rounded to 2 decimal places
        
    Raises:
        ValueError: If peso or altura are invalid (zero or negative)
    """
    if peso <= 0:
        raise ValueError("Peso deve ser maior que zero")
    if altura <= 0:
        raise ValueError("Altura deve ser maior que zero")
    
    imc = peso / (altura ** 2)
    return round(imc, 2)


def classificar_imc(imc: float) -> str:
    """
    Classify BMI value according to WHO standards.
    
    Args:
        imc: BMI value
        
    Returns:
        Classification string
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobre peso"
    elif imc < 35:
        return "Obesidade 1"
    elif imc < 40:
        return "Obesidade 2"
    else:
        return "Obesidade mórbida"
