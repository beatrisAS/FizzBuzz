<div align="center">

# ✨ FizzBuzz

### Um clássico da lógica de programação, com visual colorido no terminal

Conte de 1 a 100 e veja os múltiplos de 3 e 5 virarem **FIZZ**, **BUZZ** e **FIZZBUZZ**.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Projeto](https://img.shields.io/badge/Projeto-Educacional-8B5CF6?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-22C55E?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

O **FizzBuzz** é um exercício clássico para praticar lógica de programação. Este programa percorre os números de **1 a 100** e aplica uma regra a cada número:

- Se for múltiplo de **3**, exibe `FIZZ`.
- Se for múltiplo de **5**, exibe `BUZZ`.
- Se for múltiplo de **3 e 5 ao mesmo tempo**, exibe `FIZZBUZZ`.
- Se não atender a nenhuma dessas condições, exibe o próprio número.

Os resultados aparecem no terminal com cores ANSI. O código é introdutório e não usa funções avançadas.

## ✨ Funcionalidades

- Percorre automaticamente os números de 1 a 100.
- Identifica múltiplos de 3, de 5 e de ambos.
- Exibe cada resultado de forma organizada.
- Usa cores diferentes para destacar `FIZZ`, `BUZZ`, `FIZZBUZZ` e os números.
- Mostra a regra usada ao final da contagem.

## 🧠 Conceitos praticados

- Variáveis e atribuição de valores.
- Repetição com `for` e `range()`.
- Decisões com `if`, `elif` e `else`.
- Operadores aritméticos e resto da divisão (`%`).
- Operadores lógicos, como `and`.
- Formatação de texto com f-strings.
- Importação de variáveis de outro arquivo.
- Códigos ANSI para colorir a saída no terminal.

## 📁 Estrutura do projeto

```text
fizz_buzz/
├── main.py       # regras e exibição dos resultados
├── cores.py      # paleta de cores e estilos ANSI
└── README.md     # documentação do projeto
```

## ⚙️ Requisitos

- Python 3 instalado.
- Um terminal compatível com códigos ANSI para visualizar as cores.

Não é necessário instalar bibliotecas externas.

## ▶️ Como executar

1. Baixe ou clone este projeto.
2. Abra o terminal dentro da pasta `fizz_buzz`.
3. Execute:

```bash
python main.py
```

Se o comando `python` não funcionar, tente:

```bash
python3 main.py
```

## 🔍 Como funciona a regra

O operador `%` calcula o resto da divisão. Se o resto de `numero % 3` for zero, o número é divisível por 3. A mesma lógica vale para 5.

A condição para `FIZZBUZZ` vem primeiro, porque esses números também são divisíveis por 3 e por 5 individualmente. Assim, o programa identifica primeiro o caso mais específico.

### Exemplo da saída

```text
  1  1
  2  2
  3  FIZZ
  4  4
  5  BUZZ
  6  FIZZ
  7  7
  8  8
  9  FIZZ
 10  BUZZ
 11  11
 12  FIZZ
 13  13
 14  14
 15  FIZZBUZZ
```

No terminal, cada tipo de resultado aparece em uma cor própria.

## 🎨 Personalização das cores

As cores estão separadas no arquivo `cores.py`. O programa importa nomes que indicam seu uso, como `TITULO`, `FIZZ`, `BUZZ` e `FIZZBUZZ`.

Os códigos ANSI controlam a aparência do texto. Por exemplo, `\033[38;5;81m` escolhe uma cor ciano e `\033[0m` encerra o estilo atual. Para alterar o visual, edite os códigos no `cores.py`. A aparência pode variar conforme o terminal.

## 🔧 Ideias para versões futuras

- Permitir que a pessoa escolha o número final da contagem.
- Permitir alterar os divisores usados nas regras.
- Exibir a contagem em colunas.
- Contar quantas vezes apareceram `FIZZ`, `BUZZ` e `FIZZBUZZ`.

## 📚 Objetivo de aprendizagem

O exercício ajuda a entender como combinar repetição e condições. A ordem dos testes importa: verificar primeiro o múltiplo comum de 3 e 5 evita que ele seja identificado apenas como `FIZZ` ou `BUZZ`.

---

## 👩‍💻 Autoria

Feito por **Beatris Antunes Silva** durante o **Bootcamp de Análise de Dados da Generation Brasil**.
