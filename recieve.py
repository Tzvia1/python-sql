
import pika
from ast import literal_eval
from run_queries import run_queries

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='test')

def callback(ch, method, properties, body):
    dict = literal_eval(body.decode())
    run_queries(dict.get('con'), dict.get('output'))


channel.basic_consume(callback,
                      queue='test',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()