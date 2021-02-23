#server : ec2-cluster 

from socket import *
import numpy as np

import json

import time

port = 9999


#global serverSock
serverSock = socket(AF_INET, SOCK_STREAM)

#for port already used error
serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSock.bind(('0.0.0.0', port)) #(host, port)
serverSock.listen(1)

print('%d port access waiting...'%port)






try:

    while True:
        connectionSock, addr = serverSock.accept()

        print(str(addr), ' : accessing from.')


        recvData = connectionSock.recv(100000)

        received_data = recvData.decode('utf-8')

        ##KV get key
        received_dict = json.loads(received_data)
        print(type(received_dict))

        ##check message type
        img_str = received_dict['img']
        code_str = received_dict['code']

        img = None

        sendData = 'Result: '

        if img != -1:
            img = np.array(json.loads(img_str),dtype='float32')
            print("Image received")

            sendData += 'Image received: ' + str(img.shape) + ',  '

        if code_str != -1:
            #start -> metric -> return
            start_time = time.time()
            exec(code_str)
            end_time = time.time()

            sendData += "Excution_time: " + str(end_time - start_time)





        connectionSock.send(sendData.encode('utf-8'))
finally:
    connectionSock.close()
    serverSock.close()
    
    
    


