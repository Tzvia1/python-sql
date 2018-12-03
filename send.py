
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='test')

channel.basic_publish(exchange='',
                      routing_key='test',
                      body='{"con":"C:\sqlite\chinook.db","output":"xml"}')
channel.basic_publish(exchange='',
                      routing_key='test',
                      body='{"con":"C:\sqlite\chinook.db","output":"csv"}')
channel.basic_publish(exchange='',
                      routing_key='test',
                      body='{"con":"C:\sqlite\chinook.db","output":"tbl"}')
channel.basic_publish(exchange='',
                      routing_key='test',
                      body='{"con":"C:\sqlite\chinook.db","output":"json"}')
print(" [x] Sent 'message!'")
connection.close()