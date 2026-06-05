# Minimum Platforms

Resolução do problema **Minimum Platforms** utilizando um **algoritmo guloso**.

O objetivo do problema é determinar a quantidade mínima de plataformas necessárias para atender a uma lista de ônibus, considerando seus horários de entrada e saída.

## Informações acadêmicas

- **Aluno:** Francisco Crispim Pinto Uchôa Neto
- **Universidade:** Universidade Estadual do Ceará (UECE)
- **Disciplina:** Projeto e Análise de Algoritmos
- **Professor:** Henrique Viana

## Descrição do problema

Dado um conjunto de horários de ônibus, cada ônibus possui:

- um horário de entrada;
- um horário de saída.

O programa calcula o número mínimo de plataformas necessárias para que nenhum ônibus precise esperar por falta de plataforma disponível.

Cada linha do arquivo de entrada deve seguir o formato:

```txt
<horario_entrada> <horario_saida>
```

Os horários devem estar no formato `hh:mm`.

Exemplo:

```txt
06:10 06:45
06:00 06:25
07:30 08:10
```

## Estratégia utilizada

A solução utiliza uma abordagem gulosa:

1. Os horários de entrada são convertidos para minutos.
2. Os horários de saída também são convertidos para minutos.
3. As duas listas são ordenadas separadamente.
4. O algoritmo percorre as entradas e saídas comparando os próximos eventos:
   - se o próximo horário for uma entrada, uma plataforma é ocupada;
   - se o próximo horário for uma saída, uma plataforma é liberada.
5. A maior quantidade simultânea de plataformas ocupadas representa a resposta.

## Estrutura do projeto

```txt
.
├── minimum_platforms.py
├── messages.py
└── tests
    ├── test_0.txt
    ├── test_1.txt
    ├── test_2.txt
    └── ...
```

## Arquivos principais

### `minimum_platforms.py`

Arquivo principal do projeto. Ele contém:

- a função `hhmm_to_minutes`, que converte horários no formato `hh:mm` para minutos;
- a classe `MinimumPlatforms`, responsável por ler o arquivo de horários e calcular a solução;
- a lógica de execução via linha de comando.

### `messages.py`

Arquivo auxiliar que concentra as mensagens exibidas no terminal, como:

- mensagem de ajuda;
- título da solução;
- erro de excesso de argumentos.

### `tests/`

Diretório contendo os arquivos de teste no formato:

```txt
<entrada> <saida>
```

Os arquivos seguem o padrão de nome:

```txt
test_{num}.txt
```

Exemplo:

```txt
test_0.txt
test_1.txt
test_2.txt
```

## Como executar

### Execução padrão

Executa o programa usando o arquivo padrão:

```bash
python minimum_platforms.py
```

Por padrão, o programa utiliza:

```txt
./tests/test_0.txt
```

### Executar com um arquivo específico

```bash
python minimum_platforms.py ./tests/test_1.txt
```

Também é possível passar qualquer arquivo `.txt` que siga o formato esperado:

```bash
python minimum_platforms.py caminho/do/arquivo.txt
```

### Executar todos os testes

```bash
python minimum_platforms.py -a
```

ou:

```bash
python minimum_platforms.py --all
```

Esse comando calcula a solução para os arquivos de teste dentro do diretório `./tests/`.

### Exibir ajuda

```bash
python minimum_platforms.py -h
```

ou:

```bash
python minimum_platforms.py --help
```

## Exemplo de entrada

```txt
08:20 08:55
06:10 06:45
09:30 10:05
07:05 07:40
06:50 07:30
```

## Exemplo de saída

```txt
---------------------------- MINIMUM PLATFORMS SOLUTION ----------------------------

Quantidade mímina de plataformas para o teste padrão: 3
```

## Observações

- Os horários devem estar no formato `hh:mm`.
- Cada linha deve conter exatamente dois horários: entrada e saída.
- O algoritmo não exige que o arquivo de entrada esteja ordenado.
- Arquivos com formatação inválida podem gerar erro durante a execução.
