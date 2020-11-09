from datetime import datetime
from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)
from threading import Thread
from time import time
from typing import Any

from app.main.models import (
    MessageETHContactID
)


def handler(client_socket):
    try:
        while True:
            message = client_socket.recv(1024)
            client_socket.settimeout(60)
            if not message:
                break
            if len(message) < 20:
                continue
            else:
                message = message.decode('utf-8')
                object: int = int(message[7:11])
                type: int = 0
                if message[11] == 'E' or message[11] == '1':
                    type = 1
                if message[11] == 'R' or message[11] == '3':
                    type = 3
                if message[11] == '6':
                    type = 6
                code: int = int(message[12:15])
                area: int = int(message[15:17])
                section: int = int(message[17:20])
                time_stamp = datetime.fromtimestamp(
                    time()
                ).strftime('%Y-%m-%d %H:%M:%S')
                message = MessageETHContactID(
                    message=message,
                    user=1,
                    uid=0,
                    object=object,
                    type=type,
                    code=code,
                    area=area,
                    section=section,
                    time_stamp=time_stamp
                )
                message.save()

                # section = Section.objects.all() \
                #     .filter(object=object) \
                #     .filter(number=section)
                # status = section \
                #     .filter(AdemcoCode.objects.get())
    except Exception as e:
        raise e
    finally:
        client_socket.close()


if __name__ == '__main__':
    host: str = '0.0.0.0'
    port: int = 10008
    server: socket = socket(AF_INET, SOCK_STREAM, proto=0)
    server.bind((host, port))
    server.listen(1000)
    while True:
        client: tuple[socket, Any] = server.accept()
        thr: Thread = Thread(target=handler, args=client)
        thr.start()
