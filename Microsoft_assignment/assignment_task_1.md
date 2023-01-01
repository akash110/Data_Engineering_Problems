**Task -1**

Write a Python program that, when run on five computers, will find the smallest value in a non-empty list. The list will contain at most 2500 integer with values between 1 and 1,000,000,000. 

Each instance of your program will be called as a function 

solution(messenger, whoami) where: 

• messenger is an object responsible for accessing the list data, for sending/receiving messages between different program instances and for recording the result; 

• whoami is the ID of the program instance, numbered from 1 to 5.


The API for the messenger object is: 

• messenger.get_data_size(): returns an int stating the number of elements in the list. 

• messenger.get_item(index): gets the int at position "index" in the list. The items are numbered from 0 to size -1

• messenger.send_message( receiver, message_content): sends "message_content" to the program instance with ID "receiver". 
"receiver" has type int and "message_content" has type bytes. 

• messenger.receive_message( ): pops and returns the first message from the message queue. Multiple messages sent by one computer will be handled in the order in which they were sent. 
There is no guarantee about the order of messages sent from different computers. 
The "message_content" (of type bytes) of the message is returned. 

• messenger.record_result (result): records that result is the minimum value in the list. result should be of type int. "receiver". "receiver" has type int and "message_content" has type bytes. 

• messenger. .receive_message( ): pops and returns the first message from the message queue. Multiple messages sent by one computer will be handled in the order in which they were sent. There is no guarantee about the order of messages sent from different computers.
The "message_content" (of type bytes) of the message is returned. 

• messenger. record_result (result): records that result is the minimum value in the list. result should be of type int. 

Technical limitations: 
• message_content has to be encoded as bytes, with a maximum length of 50 bytes. Note that you can convert between str and bytes types using the encode() and decode() methods of the str or bytes object.
• Each program instance can call the messenger API at most 600 times. Above that limit, an "operations limit exceeded° exception will be raised. 
• messenger.receive message is a blocking call that waits until the queue gets a message. 
• messenger.record_result can be called only once from exactly one solution instance (it doesn't matter which instance). 

Example test cases: 

• Example 1: [1, 2, 3, 4, 5] (expected result: 1) 
• Example 2: [100, 99, 100, 99, 100, 99] (expected result: 99) 
• Example 3: [4, 4, 2, 6] (expected result: 2) 