# python-sql
The purpose of the project is creating a module that sends messages to the queue while the second module listens to the queue, when it receives the message it connects to the database and generates output types

Prerequisites
Installing:

Sqlite3

1.	http://www.sqlitetutorial.net/download-install-sqlite/
2.	http://www.sqlitetutorial.net/sqlite-sample-database/

rabbitmq

1.	https://www.rabbitmq.com/tutorials/tutorial-one-python.html
2.	https://www.rabbitmq.com/download.html
3.	http://www.erlang.org/downloads

python

1.	Python interpretr : python 3.7 : https://www.python.org/downloads/
2.	Cmd-> pip install pika

Explanation of the project

The project contains four files:
1. query.py - represents a query
2. run_queries.py - Contains the main code that receives the parameters from the message, connects to the database, runs the queries, and generates the output type
3. receive.py - A module that listens to the queue and the moment a message is received, it works accordingly
4. send.py - A module that sends messages to queue, when a message contains a path to the database and output type

Running the project

After you have downloaded all of the above installations
Run the RabbitMQ Service-start

The Python files must be run in the order specified above

The output files will be created in the c: \ sqlite folder
Where you installed the data base as specified in the installations

The tables will be created in the database

Note: For each output request, the previous output will be overwritten.


