# RabbitMQ com Python

Este projeto é um exemplo simples de comunicação assíncrona utilizando RabbitMQ e Python. Ele demonstra como enviar uma mensagem para uma fila com um produtor e consumi-la com um consumidor.

## Objetivo

O objetivo principal é mostrar na prática o fluxo básico de mensageria:

- o produtor envia uma mensagem para uma fila;
- o RabbitMQ armazena a mensagem;
- o consumidor escuta a fila e processa a mensagem.

Essa abordagem é útil para desacoplar sistemas, melhorar escalabilidade e permitir processamento assíncrono de tarefas.

## Estrutura do projeto

```text
testRabb/
├── README.md
├── .venv/
└── src/
    ├── produtor/
    │   └── produtor.py
    └── consumidor/
        └── consumidor.py
```

## Como funciona

### Produtor

O arquivo `src/produtor/produtor.py` cria uma conexão com o RabbitMQ e envia uma mensagem chamada `Hello World!` para a fila `hello`.

Fluxo:

1. Conecta ao servidor RabbitMQ localizado em `localhost`.
2. Declara a fila `hello`.
3. Publica a mensagem na fila.
4. Fecha a conexão.

### Consumidor

O arquivo `src/consumidor/consumidor.py` conecta-se ao mesmo broker, declara a fila `hello` e começa a consumir mensagens.

Fluxo:

1. Conecta ao RabbitMQ.
2. Declara a fila `hello`.
3. Define uma função de callback para processar cada mensagem recebida.
4. Inicia o consumo da fila e imprime o conteúdo da mensagem.

## Requisitos

- Python 3
- RabbitMQ em execução localmente
- Biblioteca `pika`

## Preparando o ambiente

### 1) Instalar a dependência

```bash
python -m pip install pika
```

### 2) Iniciar o RabbitMQ

Se você estiver usando Docker, pode iniciar o RabbitMQ com o seguinte comando:

```bash
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

Esse comando disponibiliza:

- porta AMQP: `5672`
- painel administrativo: `15672`

## Executando o projeto

### Rodar o produtor

```bash
python src/produtor/produtor.py
```

Esse comando envia a mensagem para a fila.

### Rodar o consumidor

```bash
python src/consumidor/consumidor.py
```

O consumidor ficará aguardando mensagens e exibirá cada uma que chegar.

## Exemplo de saída

Quando o produtor enviar a mensagem, o consumidor pode imprimir algo como:

```text
 [*] Aguardando mensagens. Para sair pressione CTRL+C
 [x] Recebido: Hello World!
```

## Observações

- O exemplo usa a fila chamada `hello`.
- A troca (`exchange`) é vazia (`''`), então a mensagem vai diretamente para a fila.
- O código usa `auto_ack=True`, ou seja, a mensagem é confirmada automaticamente após ser recebida.
- O projeto é um ponto de partida para aprender RabbitMQ com Python antes de evoluir para cenários mais complexos, como filas por prioridade, workers, DLQ e processamento distribuído.

## Próximos passos

Algumas melhorias que podem ser feitas no projeto:

- separar as configurações do RabbitMQ em um arquivo `.env`;
- criar classes para produtor e consumidor;
- implementa logs estruturados;
- tratar rejeição de mensagens e retries;
- adicionar múltiplos consumidores e filas diferentes.

## Licença

Este projeto é um exemplo educativo e pode ser usado livremente para estudo e aprendizado.
