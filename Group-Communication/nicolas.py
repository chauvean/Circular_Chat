# import sys
import threading

import Pyro4

from client import Client


class request_loop(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        daemon.requestLoop()


class send_request(threading.Thread):
    """
    wait for request as input
    Broadcast this message to the server
    Loops
    """
    def __init__(self, uri, client_id):  # jusqua = donnée supplémentaire
        threading.Thread.__init__(self)  # ne pas oublier cette ligne
        # (appel au constructeur de la classe mère)
        self.uri = uri
        self.cid = client_id
        self._is_running = True

    def stop(self):
        self._is_running = False

    def run(self):
        proxy = Pyro4.Proxy(uri)
        while self._is_running:
            request = input()
            if request == "leave":
                self.stop()
                print(self._is_running)
                # proxy.leave_chat(server)
            else:
                proxy.broadcast(server, request, self.cid)

"""
Create Server Proxy
register client through daemon object into nameserver
ask server to join chat
launch thread to send messages
Wait for incoming requests
"""

# sys.excepthook = Pyro4.util.excepthook
daemon = Pyro4.Daemon()
server = Pyro4.Proxy("PYRONAME:main.server")
member = Client()  # create client instance
uri = daemon.register(member)  # create the link to make it accessible from outside
print(uri)
ns = Pyro4.locateNS()
ns.register("nicolas", uri)  # register object onto the server
client_id = member.ask_to_join_chat(server, "nicolas")

m = send_request(uri, client_id)
m.start()

daemon.requestLoop()
