#initialize any zmq libs
import zmq
print zmq.pyzmq_version()
import time
import sys

port = "5556"

#we want to run the server on multiple ports(so request can be distributed)
if len(sys.argv) >1;
	port = sys.argv[1]
	print port
	int(port)
#multiple contexts can be created in an app.
#contexts are thread-safe unlike sockets
context = zmq.Context()

#create REP socket from the context
socket = context.socket(zmq.REP)
#bind socket to port
socket.bind("tcp://*:%s" % port)

while True:
	#wait for request
	message = socket.recv()
	print "Received client request" , message

	time.sleep(1)
	socket.send("Server got your request, here's your response from %s" %port)
