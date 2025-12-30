# Calculadora de IMC (Índice de Massa Corporal)

## 📋 Descrição

Este é um programa simples em Python que calcula o **Índice de Massa Corporal (IMC)** de uma pessoa. O IMC é uma medida internacional usada para avaliar se uma pessoa está no peso ideal, considerando sua altura e peso.

## 🧮 Como Funciona

O programa utiliza a fórmula padrão do IMC:

```
IMC = peso (kg) / altura² (m)
```

Após calcular o IMC, o programa classifica o resultado de acordo com as categorias estabelecidas pela Organização Mundial da Saúde (OMS):

| IMC | Classificação |
|-----|---------------|
| Abaixo de 18,5 | Abaixo do peso |
| 18,5 - 24,9 | Peso normal |
| 25,0 - 29,9 | Sobrepeso |
| 30,0 - 34,9 | Obesidade Grau I |
| 35,0 - 39,9 | Obesidade Grau II |
| 40,0 ou mais | Obesidade Mórbida (Grau III) |

## 🚀 Como Usar

### Pré-requisitos

- Python 3.x instalado no seu computador

### Executando o Programa

1. Clone este repositório:
```bash
git clone https://github.com/wallacedeveloper/Calculadora-IMC.git
```

2. Navegue até o diretório do projeto:
```bash
cd Calculadora-IMC
```

3. Execute o programa:
```bash
python calculadora_imc.py
```

4. Digite seu peso em quilogramas (kg) quando solicitado
5. Digite sua altura em metros (m) quando solicitado
6. O programa exibirá seu IMC e a classificação correspondente

### Exemplo de Uso

```
Digite seu peso em Kg: 70
Digite sua altura: 1.75
Seu IMC é: 22.86
Peso normal
```

## 📝 Estrutura do Código

O programa é composto por:

1. **Entrada de Dados**: Solicita ao usuário o peso e altura
2. **Cálculo do IMC**: Aplica a fórmula matemática (peso / altura²)
3. **Formatação**: Arredonda o resultado para 2 casas decimais
4. **Classificação**: Utiliza estruturas condicionais (if/elif/else) para determinar a categoria do IMC
5. **Saída**: Exibe o valor do IMC e sua classificação

## 🛠️ Tecnologias

- **Python 3**: Linguagem de programação utilizada
- Funções nativas: `input()`, `float()`, `round()`, `print()`

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

Wallace Martins - [wallacedeveloper](https://github.com/wallacedeveloper)

## ⚠️ Observações

- Este programa é apenas para fins educacionais e informativos
- O IMC não deve ser usado como única ferramenta para diagnóstico de saúde
- Consulte sempre um profissional de saúde para avaliação completa
