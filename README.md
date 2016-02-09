# zeromq-request-reply-pyzmq
Request/reply pattern (client/server) in python &amp; zeromq

In this pattern, client sends a request and server replies to the request. Request sockets can connect to many servers and will be distributed to all of the servers. Request sockets will block on send if it doesn't get a reply. Replies will block on receive until a request is received. Requests and responses must be paired & successful.

To run, start up two servers on two separate ports:<br/>
python zmq-response-server.py 5546<br/>
python zmq-response-server.py 5556<br/>
And then run client ot send requests to them.
python zmq-request-client.py 5546 5556