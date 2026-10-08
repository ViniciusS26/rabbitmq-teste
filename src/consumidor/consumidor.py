import pika
import sys
import os

def main():
    # 1. Conectar ao servidor
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # 2. Garantir que a fila existe
    channel.queue_declare(queue='hello')

    # 3. Definir a função que processa a mensagem recebida
    def callback(ch, method, properties, body):
        print(f" [x] Recebido: {body.decode()}")

    # 4. Indicar ao RabbitMQ qual função deve ler a fila 'hello'
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Aguardando mensagens. Para sair pressione CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Encerrando...')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
