import threading

import Pyro4.util

from client import Client


class request_loop(threading.Thread):
    """
    launch thread waiting
    for outside requests
    """
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
    def __init__(self, uri, client_id):
        threading.Thread.__init__(self)
        self.uri = uri
        self.cid = client_id

    def run(self):
        proxy = Pyro4.Proxy(uri)
        while (True):
            request = input()
            if request == "leave":
                proxy.leave_chat(server)
            else:
                proxy.broadcast(server, request, self.cid)


daemon = Pyro4.Daemon()
server = Pyro4.Proxy("PYRONAME:main.server")
member = Client()
uri = daemon.register(member)
print(uri)
ns = Pyro4.locateNS()
ns.register("remi", uri)
client_id = member.ask_to_join_chat(server, "remi")
m = send_request(uri, client_id)
m.start()

daemon.requestLoop()
