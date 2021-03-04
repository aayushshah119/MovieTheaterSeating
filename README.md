# Movie-Theatre-Seating-Arrangement
An algorithm for assigning seats within a movie theater to fulfill reservation requests while maximizing both customer satisfaction and customer safety.

 ## Input: 

An input file which would contain one line of input for each reservation request. The order of the lines in the file reflects the order in which the reservation requests were received. Each line in the file will be comprised of a reservation identifier, followed by a space, and then the number of seats requested. The reservation identifier will have the format: R####.
Example: 
R001 2 
R002 4 
R003 4 
R004 3
...

 ## Output: 

The program should output a file containing the seating assignments for each request. Each row in the file should include the reservation number followed by a space, and then a comma-delimited list of the assigned seats.
Example: 
R001 I1,I2
R002 F16,F17,F18,F19 
R003 A1,A2,A3,A4 
R004 J4,J5,J6
...

 ## Assumptions:
1. Quality of seats increases with distance from the screen. Example: Seats in J row are considered to be better than those in A row.
2. Customer satisfaction is determined by                                   
   (1) Being allocated continuos seats in one row  
   (2) Get the better quality seats
   (3) Being allocated seats even if seats are allocated in seperate row
3. Cost of all the seats in the theatre are same. 
4. Seats are reserved on the first come first serve basis. 
5. Customers who reserves the seat first are offered better seats(seats that are far from the screen) than the customers who are reserve later. 
6. When no row is empty and only vacant seats need to be full filled reservation that suits the both sattisfaction are selected first.  
8. Every booking wants to get the seats even if the seats allocated are in seperate rows. 
9. If there aren't enough seats available, then no seat is assigned and we go to the next reservation request.

 ## Instructions for building the solution:
 1. Used a greedy algorithm based approach to assign seats. Assignment is done to maximize the customer satisfaction.
 2. Represented the movie theater as a list of Row objects. Each Row object has a pointer to the available seats.
 3. Given the number of seats, find the furthest row from the screen that can accomodate the required seats. If no single row has the capacity to accomodate everyone, then start assignning as many seats as possible from the furthest row. 
 4. As you assign seats in one row, update the class attributes of seat_pointer and number of empty seats
 5. If the total number of required seats is greater than the empty seats in the theater, then skip that reservation. 

 ## Program Files: 
 1. cli.py: The command line interface. This file reads the input and writes to the output file.
 2. MovieTheaterSeating.py: Uses the algorithm to allocate seats
 3. Testing.py: Uses PyTest to test individual methods of Theater class as well as integrated tests.

 ## How to run the program: 
 1. Open Command prompt or terminal. 
 2. Move to the directory where the program is stored. Make sure all the program files are in the same folder before running the program.
 3. The program accepts text files where *each line* in the file will have a reservation identifier, followed by a space, and then the number of seats requested. The reservation identifier will have the format: R####. as displayed above. 
 4. Ensure python module logging is present.
 5. Type the following command in the  command prompt or terminal. 
 ```bash
python cli.py *inputFilePath*
```
            
6. If no seats can be allocated for a reservation id, a message like "Not enough seats for *ReservationID*. The program terminates with the location of the output file from the current directory.


 ## How to run the test:
1. Install the requirements using pip:
```bash
pip3 install -U pytest
```

2. Run the command below to run all the tests. I have used the pytest module for testing of this project. 
```bash
pytest Testing.py
```
 ## Improvement for the current algorithm:
1. Create a heuristic for each segment of customer satisfaction. By doing this, we can choose to prioritize one aspect at the cost other. For example, if being seated in seat J vs seat I hardly makes a difference as compared to everyone seating together, then we can first choose to accomodate the biggest group and assign them seats rather than to those who come first.
2. Since this is a derivate of constraint optimization problem, it is possible to have a backtracking based algorithm to search through all possible combinations of arrangements and then choose the one with the maximize customer satisfaction while maintaing customer safety.

 
