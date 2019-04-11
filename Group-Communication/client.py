
import Pyro4



@Pyro4.expose
class Client:
    def __init__(self):
        self.nom = "default name"
        self.my_uri = "default uri"
        self.client_id = -1

    def broadcast(self, server, message, client_id):
        """
        asks server to broadcast message to all clients
        """
        server.broadcast_message_from_client_v2(client_id, message)

    def ask_to_join_chat(self, server, nom):
        client_id = server.join_chat(
            nom)  # we could add a list of valid names in the server, for instance I only want andeol nicolas and remi to join
        return client_id

    def leave_chat(self, server):
        server.ask_to_leave_chat(self.client_id)

    @Pyro4.expose
    def receive_message(self, message):
        """
        Print message transmitted by server
        Could check if message not directly from another client
        """
        print("\n" + message)
