# Circular_Chat
CIrculat Chat application from Distributed Systems Course

Lanch a remote client :

Procedure in


Launch a remote client :

    daemon = Pyro4.Daemon() #launch daemon object
    nicolas = Clodo('nicolas') #create client instance
    uri = daemon.register(nicolas) #create the link to make it accessible from outside
    print(uri)
    ns = Pyro4.locateNS()
    ns.register("nicolas", uri) #register object onto the server
    daemon.requestLoop() #waits for any request from the outside


What Chat  can do :

Join CHat
Wait for input request and send messages
