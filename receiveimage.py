import pika, ast
import pika, os, sys, json
import time


#import PyQt5
from PyQt5 import QtGui
from PyQt5 import QtWidgets




import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QLabel,QPushButton
#from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap


class MetaClass(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class RabbitMqServerConfigure(metaclass = MetaClass):

    def __init__(self, host = 'localhost', queue = 'hello'):

        self.host = host
        self.queue = queue


class rabbitmqServer():

    def __init__(self, server):

        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host = self.server.host))
        self._channel = self._connection.channel()
        self._tem = self._channel.queue_declare(queue = self.server.queue)
        print("Server started waiting for messages")

    @staticmethod
    def callback(ch, method, properties, body):

        Payload = body.decode('utf-8')
        Payload = ast.literal_eval(Payload)
        

        with open('received.png', 'wb') as f:
            f.write(Payload)

        with open('config.txt','w') as g:
            g.write("True")

        
        

    def startserver(self):
        self._channel.basic_consume(
                    queue = self.server.queue,
                    on_message_callback=rabbitmqServer.callback,
                    auto_ack = True   
        )
        self._channel.start_consuming()



def main():
    
    with open('config.txt','w') as f:
        f.write("False")
    
    serverconfigure = RabbitMqServerConfigure(host = 'localhost', queue = 'hello')
    server = rabbitmqServer(server = serverconfigure)
    server.startserver()


    

        
    
