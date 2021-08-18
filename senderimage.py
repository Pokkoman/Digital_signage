import pika, os, sys, json
import time

class MetaClass(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class RabbitmqConfigure(metaclass = MetaClass):

    def __init__(self, queue = 'hello', host = 'localhost', routingKey = 'hello', exchange = ''):
        self.queue = queue
        self.host = host
        self.routingKey = routingKey
        self.exchange = exchange


class RabbitMq():

    __slots__ = ["server", "_channel", "_connection"]

    def __init__(self, server):


        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host = self.server.host))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue = self.server.queue)

    def __enter__(self):
        #print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #print("__exit__")
        self._connection.close()

    
    def publish(self, payload = {}):
        self._channel.basic_publish(exchange = self.server.exchange,
                                    routing_key=self.server.routingKey,
                                    body = str(payload))

        #print("Published Message: {}".format(payload))


class Image(object):
    __slots__ = ["filename"]

    def __init__(self, filename):
        self.filename = filename

    @property
    def get(self):
        with open(self.filename, 'rb') as f:
            data = f.read()
        return data


if __name__ == '__main__':

    server = RabbitmqConfigure(queue = 'hello',
                               host = 'localhost',
                               routingKey = 'hello',
                               exchange = '')

    image = Image(filename = r'C:\Users\Surit\Documents\PythonProjects\rabbitmq\customer1.png')
    data = image.get

    image2 = Image(filename = r'C:\Users\Surit\Documents\PythonProjects\rabbitmq\customer2.png')
    data2 = image2.get

    image3 = Image(filename = r'C:\Users\Surit\Documents\PythonProjects\rabbitmq\customer3.png')
    data3 = image3.get

    with RabbitMq(server) as rabbitmq:
        rabbitmq.publish(payload = data)      
        print("sent data1")

        time.sleep(15)        

        rabbitmq.publish(payload = data2)      
        print("done sending data")

 

