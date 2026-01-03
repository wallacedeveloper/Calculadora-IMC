# Examples and Screenshots

## Command Line Interface (CLI)

```bash
$ python -m src.calculadora_imc.cli
=== Calculadora de IMC ===

Digite seu peso em Kg: 70
Digite sua altura em metros: 1.75

Seu IMC é: 22.86
Classificação: Peso normal
```

## Flask Web API

### Web Interface
When you navigate to `http://127.0.0.1:5000/` in your browser, you'll see:
- A clean, responsive web interface
- Input fields for weight (kg) and height (m)
- A "Calcular IMC" button
- Result display showing IMC value and classification
- API documentation section

### API Response Example
```bash
$ curl -X POST http://127.0.0.1:5000/api/calcular \
  -H "Content-Type: application/json" \
  -d '{"peso": 70, "altura": 1.75}'

{
  "imc": 22.86,
  "classificacao": "Peso normal"
}
```

## Tkinter GUI

The GUI application provides:
- Clean window titled "Calculadora de IMC"
- Input fields for:
  - Peso (kg): Text entry field
  - Altura (m): Text entry field
- Green "Calcular IMC" button
- Result display showing:
  - IMC value
  - Classification

The GUI uses a modern, user-friendly design with proper error handling and validation.

## Test Output

```bash
$ pytest tests/ -v
================================================= test session starts ==================================================
platform linux -- Python 3.12.3, pytest-9.0.2, pluggy-1.6.0
collected 27 items

tests/test_calculator.py::TestCalcularIMC::test_calculo_normal PASSED                          [  3%]
tests/test_calculator.py::TestCalcularIMC::test_calculo_arredondamento PASSED                  [  7%]
tests/test_calculator.py::TestCalcularIMC::test_calculo_peso_baixo PASSED                      [ 11%]
tests/test_calculator.py::TestCalcularIMC::test_calculo_peso_alto PASSED                       [ 14%]
tests/test_calculator.py::TestCalcularIMC::test_peso_zero PASSED                               [ 18%]
tests/test_calculator.py::TestCalcularIMC::test_peso_negativo PASSED                           [ 22%]
tests/test_calculator.py::TestCalcularIMC::test_altura_zero PASSED                             [ 25%]
tests/test_calculator.py::TestCalcularIMC::test_altura_negativa PASSED                         [ 29%]
tests/test_calculator.py::TestCalcularIMC::test_valores_muito_pequenos PASSED                  [ 33%]
tests/test_calculator.py::TestCalcularIMC::test_valores_muito_grandes PASSED                   [ 37%]
tests/test_calculator.py::TestClassificarIMC::test_abaixo_do_peso_limite_inferior PASSED       [ 40%]
tests/test_calculator.py::TestClassificarIMC::test_abaixo_do_peso_limite_superior PASSED       [ 44%]
tests/test_calculator.py::TestClassificarIMC::test_peso_normal_limite_inferior PASSED          [ 48%]
tests/test_calculator.py::TestClassificarIMC::test_peso_normal_medio PASSED                    [ 51%]
tests/test_calculator.py::TestClassificarIMC::test_peso_normal_limite_superior PASSED          [ 55%]
tests/test_calculator.py::TestClassificarIMC::test_sobre_peso_limite_inferior PASSED           [ 59%]
tests/test_calculator.py::TestClassificarIMC::test_sobre_peso_limite_superior PASSED           [ 62%]
tests/test_calculator.py::TestClassificarIMC::test_obesidade_1_limite_inferior PASSED          [ 66%]
tests/test_calculator.py::TestClassificarIMC::test_obesidade_1_limite_superior PASSED          [ 70%]
tests/test_calculator.py::TestClassificarIMC::test_obesidade_2_limite_inferior PASSED          [ 74%]
tests/test_calculator.py::TestClassificarIMC::test_obesidade_2_limite_superior PASSED          [ 77%]
tests/test_calculator.py::TestClassificarIMC::test_obesidade_morbida_limite_inferior PASSED    [ 81%]
tests/test_calculator.py::TestClassificarIMC::test_obesidade_morbida_valor_alto PASSED         [ 85%]
tests/test_calculator.py::TestClassificarIMC::test_obesidade_morbida_valor_muito_alto PASSED   [ 88%]
tests/test_calculator.py::TestIntegracao::test_fluxo_completo_normal PASSED                    [ 92%]
tests/test_calculator.py::TestIntegracao::test_fluxo_completo_sobrepeso PASSED                 [ 96%]
tests/test_calculator.py::TestIntegracao::test_fluxo_completo_obesidade PASSED                 [100%]

================================================== 27 passed in 0.04s ==================================================
```

All 27 tests pass successfully, covering:
- Normal BMI calculations
- Rounding to 2 decimal places
- Edge cases (very small/large values)
- Error handling (zero and negative values)
- All BMI classification ranges
- Integration tests for complete workflow
