"""
Unit tests for BMI Calculator.
"""
import pytest
from src.calculadora_imc.calculator import calcular_imc, classificar_imc


class TestCalcularIMC:
    """Test cases for calcular_imc function."""
    
    def test_calculo_normal(self):
        """Test normal BMI calculation."""
        imc = calcular_imc(70, 1.75)
        assert imc == 22.86
    
    def test_calculo_arredondamento(self):
        """Test BMI rounding to 2 decimal places."""
        imc = calcular_imc(80, 1.80)
        assert imc == 24.69
    
    def test_calculo_peso_baixo(self):
        """Test BMI calculation with low weight."""
        imc = calcular_imc(50, 1.70)
        assert imc == 17.30
    
    def test_calculo_peso_alto(self):
        """Test BMI calculation with high weight."""
        imc = calcular_imc(120, 1.65)
        assert imc == 44.08
    
    def test_peso_zero(self):
        """Test that zero weight raises ValueError."""
        with pytest.raises(ValueError, match="Peso deve ser maior que zero"):
            calcular_imc(0, 1.75)
    
    def test_peso_negativo(self):
        """Test that negative weight raises ValueError."""
        with pytest.raises(ValueError, match="Peso deve ser maior que zero"):
            calcular_imc(-70, 1.75)
    
    def test_altura_zero(self):
        """Test that zero height raises ValueError."""
        with pytest.raises(ValueError, match="Altura deve ser maior que zero"):
            calcular_imc(70, 0)
    
    def test_altura_negativa(self):
        """Test that negative height raises ValueError."""
        with pytest.raises(ValueError, match="Altura deve ser maior que zero"):
            calcular_imc(70, -1.75)
    
    def test_valores_muito_pequenos(self):
        """Test BMI calculation with very small values."""
        imc = calcular_imc(0.5, 0.1)
        assert imc == 50.0
    
    def test_valores_muito_grandes(self):
        """Test BMI calculation with very large values."""
        imc = calcular_imc(200, 2.0)
        assert imc == 50.0


class TestClassificarIMC:
    """Test cases for classificar_imc function."""
    
    def test_abaixo_do_peso_limite_inferior(self):
        """Test underweight classification at lower boundary."""
        assert classificar_imc(15.0) == "Abaixo do peso"
    
    def test_abaixo_do_peso_limite_superior(self):
        """Test underweight classification at upper boundary."""
        assert classificar_imc(18.4) == "Abaixo do peso"
    
    def test_peso_normal_limite_inferior(self):
        """Test normal weight classification at lower boundary."""
        assert classificar_imc(18.5) == "Peso normal"
    
    def test_peso_normal_medio(self):
        """Test normal weight classification in the middle."""
        assert classificar_imc(22.0) == "Peso normal"
    
    def test_peso_normal_limite_superior(self):
        """Test normal weight classification at upper boundary."""
        assert classificar_imc(24.9) == "Peso normal"
    
    def test_sobre_peso_limite_inferior(self):
        """Test overweight classification at lower boundary."""
        assert classificar_imc(25.0) == "Sobre peso"
    
    def test_sobre_peso_limite_superior(self):
        """Test overweight classification at upper boundary."""
        assert classificar_imc(29.9) == "Sobre peso"
    
    def test_obesidade_1_limite_inferior(self):
        """Test obesity class 1 at lower boundary."""
        assert classificar_imc(30.0) == "Obesidade 1"
    
    def test_obesidade_1_limite_superior(self):
        """Test obesity class 1 at upper boundary."""
        assert classificar_imc(34.9) == "Obesidade 1"
    
    def test_obesidade_2_limite_inferior(self):
        """Test obesity class 2 at lower boundary."""
        assert classificar_imc(35.0) == "Obesidade 2"
    
    def test_obesidade_2_limite_superior(self):
        """Test obesity class 2 at upper boundary."""
        assert classificar_imc(39.9) == "Obesidade 2"
    
    def test_obesidade_morbida_limite_inferior(self):
        """Test morbid obesity at lower boundary."""
        assert classificar_imc(40.0) == "Obesidade mórbida"
    
    def test_obesidade_morbida_valor_alto(self):
        """Test morbid obesity with high value."""
        assert classificar_imc(50.0) == "Obesidade mórbida"
    
    def test_obesidade_morbida_valor_muito_alto(self):
        """Test morbid obesity with very high value."""
        assert classificar_imc(100.0) == "Obesidade mórbida"


class TestIntegracao:
    """Integration tests combining calculation and classification."""
    
    def test_fluxo_completo_normal(self):
        """Test complete flow with normal weight."""
        imc = calcular_imc(70, 1.75)
        classificacao = classificar_imc(imc)
        assert imc == 22.86
        assert classificacao == "Peso normal"
    
    def test_fluxo_completo_sobrepeso(self):
        """Test complete flow with overweight."""
        imc = calcular_imc(85, 1.75)
        classificacao = classificar_imc(imc)
        assert imc == 27.76
        assert classificacao == "Sobre peso"
    
    def test_fluxo_completo_obesidade(self):
        """Test complete flow with obesity."""
        imc = calcular_imc(100, 1.75)
        classificacao = classificar_imc(imc)
        assert imc == 32.65
        assert classificacao == "Obesidade 1"
