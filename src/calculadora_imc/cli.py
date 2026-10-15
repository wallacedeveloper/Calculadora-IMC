"""
Command-line interface for BMI Calculator.
"""
from .calculator import calcular_imc, classificar_imc


def main():
    """Main CLI interface for BMI calculator."""
    print("=== Calculadora de IMC ===")
    print()
    
    try:
        peso = float(input('Digite seu peso em Kg: '))
        altura = float(input('Digite sua altura em metros: '))
        
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        
        print()
        print(f'Seu IMC é: {imc}')
        print(f'Classificação: {classificacao}')
        
    except ValueError as e:
        print(f'Erro: {e}')
    except Exception as e:
        print(f'Erro inesperado: {e}')


if __name__ == "__main__":
    main()
