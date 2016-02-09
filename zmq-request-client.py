#initialize any zmq libs
import zmq
print zmq.pyzmq_version()
import time
import sys

port = "5556"

#we want to send to two different servers, here's the logic
if len(sys.argv) > 1:
	port = sys.argv[1]
	print "sending request on port" + port
	int(port)

if len(sys.argv) > 2:
	port1 = sys.argv[2]
	print "sending request onport" + port1
	int(port1)

context = zmq.Context()
#create REQ socket from the contex
print "connecting to server ..."
socket = context.socket(zmq.REQ)

#connect socket to port
#we created two server ports, this single socket
#is able to connect to both
socket.connect("tcp://localhost:%s" % port)
if len(sys.argv)>2:
	socket.connect("tcp://localhost:%s" % port1)


for request in range (1,100):
	print "Sending client request ", request, '...'
	socket.send("Client sending request");
	#get reply
	message = socket.recv()
	print "Got reply from server", request, "[", message, "]"