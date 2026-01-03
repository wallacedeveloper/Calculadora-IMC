Calculadora de IMC (BMI Calculator)

[![CI Tests](https://github.com/wallacedeveloper/Calculadora-IMC/actions/workflows/ci.yml/badge.svg)](https://github.com/wallacedeveloper/Calculadora-IMC/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Uma calculadora completa de IMC (Índice de Massa Corporal) desenvolvida em Python com múltiplas interfaces: linha de comando (CLI), interface gráfica (GUI) e API REST.

## 📋 Sobre o Projeto

O IMC (Índice de Massa Corporal) é uma medida internacional usada para calcular se uma pessoa está no peso ideal. Ele é calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).

Este projeto oferece uma implementação completa com:
- 🧮 Cálculo preciso de IMC
- 📊 Classificação segundo padrões da OMS (Organização Mundial da Saúde)
- 💻 Interface de linha de comando
- 🖼️ Interface gráfica com Tkinter
- 🌐 API REST com Flask
- ✅ Testes automatizados
- 🔄 CI/CD com GitHub Actions

### Classificação do IMC

| IMC | Classificação |
|-----|---------------|
| < 18.5 | Abaixo do peso |
| 18.5 - 24.9 | Peso normal |
| 25.0 - 29.9 | Sobre peso |
| 30.0 - 34.9 | Obesidade Grau 1 |
| 35.0 - 39.9 | Obesidade Grau 2 |
| ≥ 40.0 | Obesidade Mórbida |

## 🚀 Como Começar

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/wallacedeveloper/Calculadora-IMC.git
cd Calculadora-IMC
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv

# No Windows:
venv\Scripts\activate

# No Linux/Mac:
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 💡 Como Usar

### Interface de Linha de Comando (CLI)

Execute o script CLI para uma experiência interativa no terminal:

```bash
python -m src.calculadora_imc.cli
```

Você será solicitado a inserir seu peso e altura, e o programa calculará seu IMC.

### Interface Gráfica (GUI)

Inicie a interface gráfica com Tkinter:

```bash
python -m src.calculadora_imc.gui
```

Uma janela será aberta onde você pode inserir seus dados e calcular o IMC com um clique.

### API REST (Flask)

Inicie o servidor Flask:

```bash
python -m src.calculadora_imc.api
```

O servidor estará disponível em `http://127.0.0.1:5000` por padrão.

#### Variáveis de Ambiente (Opcionais)

Você pode configurar o servidor Flask usando variáveis de ambiente:

```bash
# Habilitar modo debug (não use em produção!)
export FLASK_DEBUG=true

# Configurar host (padrão: 127.0.0.1)
export FLASK_HOST=0.0.0.0

# Configurar porta (padrão: 5000)
export FLASK_PORT=8080

python -m src.calculadora_imc.api
```

#### Endpoints da API

**Interface Web**
```
GET http://localhost:5000/
```
Acesse pelo navegador para usar a interface web interativa.

**Calcular IMC**
```
POST http://localhost:5000/api/calcular
Content-Type: application/json

{
  "peso": 70,
  "altura": 1.75
}
```

Resposta:
```json
{
  "imc": 22.86,
  "classificacao": "Peso normal"
}
```

**Health Check**
```
GET http://localhost:5000/health
```

### Como Biblioteca Python

Você também pode usar a calculadora como uma biblioteca em seus próprios projetos:

```python
from src.calculadora_imc import calcular_imc, classificar_imc

# Calcular IMC
peso = 70  # kg
altura = 1.75  # metros
imc = calcular_imc(peso, altura)

# Obter classificação
classificacao = classificar_imc(imc)

print(f"IMC: {imc}")
print(f"Classificação: {classificacao}")
```

## 🧪 Testes

O projeto inclui uma suíte completa de testes automatizados usando pytest.

### Executar todos os testes:
```bash
pytest
```

### Executar testes com cobertura:
```bash
pytest --cov=src.calculadora_imc --cov-report=html
```

### Executar testes específicos:
```bash
pytest tests/test_calculator.py::TestCalcularIMC::test_calculo_normal
```

Os testes cobrem:
- ✅ Cálculos de IMC com diversos valores
- ✅ Classificações em todas as faixas
- ✅ Casos de borda e validação de entrada
- ✅ Tratamento de erros

## 📁 Estrutura do Projeto

```
Calculadora-IMC/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD
├── src/
│   └── calculadora_imc/
│       ├── __init__.py         # Inicialização do pacote
│       ├── calculator.py       # Lógica principal de cálculo
│       ├── cli.py              # Interface de linha de comando
│       ├── gui.py              # Interface gráfica (Tkinter)
│       └── api.py              # API REST (Flask)
├── tests/
│   ├── __init__.py
│   └── test_calculator.py      # Testes automatizados
├── calculadora_imc.py          # Script original (mantido para compatibilidade)
├── requirements.txt            # Dependências do projeto
├── README.md                   # Este arquivo
└── LICENSE                     # Licença MIT
```

## 🤝 Como Contribuir

Contribuições são bem-vindas! Siga estas etapas para contribuir:

1. **Fork o projeto**
   - Clique no botão "Fork" no topo da página

2. **Clone seu fork**
   ```bash
   git clone https://github.com/seu-usuario/Calculadora-IMC.git
   cd Calculadora-IMC
   ```

3. **Crie uma branch para sua feature**
   ```bash
   git checkout -b feature/minha-nova-feature
   ```

4. **Faça suas alterações**
   - Escreva código limpo e bem documentado
   - Adicione testes para novas funcionalidades
   - Certifique-se de que todos os testes passam

5. **Commit suas mudanças**
   ```bash
   git add .
   git commit -m "Adiciona minha nova feature"
   ```

6. **Push para seu fork**
   ```bash
   git push origin feature/minha-nova-feature
   ```

7. **Abra um Pull Request**
   - Vá até o repositório original
   - Clique em "New Pull Request"
   - Descreva suas alterações detalhadamente

### Diretrizes de Contribuição

- ✅ Mantenha o código Python seguindo PEP 8
- ✅ Adicione testes para novas funcionalidades
- ✅ Atualize a documentação quando necessário
- ✅ Certifique-se de que o CI passa
- ✅ Use mensagens de commit descritivas

### Reportar Bugs

Encontrou um bug? Abra uma [issue](https://github.com/wallacedeveloper/Calculadora-IMC/issues) com:
- Descrição clara do problema
- Passos para reproduzir
- Comportamento esperado vs. atual
- Screenshots (se aplicável)

## 🔄 CI/CD

O projeto utiliza GitHub Actions para integração e entrega contínuas. A cada push ou pull request:
- ✅ Testes automatizados são executados
- ✅ Código é verificado em múltiplas versões do Python
- ✅ Relatórios de cobertura são gerados

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

**Wallace Martins**

- GitHub: [@wallacedeveloper](https://github.com/wallacedeveloper)

## 🙏 Agradecimentos

- Organização Mundial da Saúde (OMS) pelos padrões de classificação de IMC
- Comunidade Python pelo excelente ecossistema de ferramentas
- Todos os contribuidores que ajudarem a melhorar este projeto

## 📚 Recursos Adicionais

- [Documentação Python](https://docs.python.org/3/)
- [Documentação Flask](https://flask.palletsprojects.com/)
- [Documentação Pytest](https://docs.pytest.org/)
- [Informações sobre IMC - OMS](https://www.who.int/health-topics/obesity)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no GitHub!
