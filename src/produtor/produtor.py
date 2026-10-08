import pika

# 1. Conectar ao servidor RabbitMQ que está no Docker
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 2. Criar a fila onde a mensagem será guardada
channel.queue_declare(queue='hello')

# 3. Enviar a mensagem para a fila
mensagem = "Hello World!"
channel.basic_publish(exchange='', routing_key='hello', body=mensagem)
print(f" [x] Enviado: '{mensagem}'")

# 4. Fechar a conexão
connection.close()