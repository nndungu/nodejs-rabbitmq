
import pika, sys, os

host = 'localhost'
queue = 'my-queue'

def on_message(ch, method, properties, body):
    message = body.decode('utf-8')
    print(message)

def main():
    connection_params = pika.ConnectionParameters(host=host)
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue=queue)
    channel.basic_consume(queue=queue, on_message_callback=on_message, auto_ack=True)

    print('Subscribed to ' + queue + ', waiting for message...')
    channel.start_consuming()

if __name__ == '__main__':
    main()