from __future__ import print_function

from random import randint

import Pyro4.util

ns = Pyro4.locateNS()


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Server(object):
    def __init__(self):
        self.members = dict()

    @Pyro4.expose
    def join_chat(self, nom):
        new_id = self.give_correct_id()
        uri = ns.lookup(nom)
        self.members[new_id] = uri
        return new_id

    def give_correct_id(self):
        new_id = randint(1, 10000)
        while new_id in self.members:
            new_id = randint(1, 10000)
        return new_id


    @Pyro4.expose
    def ask_to_leave_chat(self, cid):
        """
        removes id+uri from the dict of members
        """
        del self.members[cid]

    @Pyro4.expose
    def broadcast_message_from_client_v2(self, client_id, message):
        """
        Checks if client allowed in the chat
        Send to all elements in self.members
        """
        if client_id in self.members:
            for key in self.members:
                if key != client_id:
                    proxy = Pyro4.Proxy(self.members[key])
                    proxy.receive_message(message)
        else:
            return "Please register first"


def main():
    Pyro4.Daemon.serveSimple(
        {
            Server: "main.server"
        },
        ns=True)


if __name__ == "__main__":
    main()
