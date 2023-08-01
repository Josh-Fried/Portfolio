


https://github.com/Josh-Fried/Portfolio/assets/98046392/bfd498d8-d7ce-48af-9e56-90e1a7496884



Link Layer Token Passing Protocol, Created by: Josh Fried and Jeremy Heng

Instructions:

1. Make sure all nodes (head and non-head nodes) involved are setup in a ring topology with their sending and receiving ports
	- this will have to be done before or while setting up all the nodes
2. Start non-head nodes w/ node.py
	- execute node.py with 5 command line arguments: 
		- <node's sending port> <node's receiving port> <# of packets to start in node's buffer> <1 if head, 0 if not head> <node #/ID>
	- e.g. for non-head node: python3 node.py 8081 8080 5 0 2
3. Start head node w/ node.py
	- execute node.py with 5 command line arguments: 
		- <node's sending port> <node's receiving port> <# of packets to start in node's buffer> <1 if head, 0 if not head> <node #/ID>
	- e.g. for head node: python3 node.py 8081 8080 5 1 1
3. System will run forever if untouched, will not terminate gracefully
	- terminate each node instance, if you want to run the system again
	- repeat instructions






