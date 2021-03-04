""" This file handles the command line arguments. It also reads and writes file.
After book() method from MovieTheater class returns a string or None, it writes it
to the output file. """

import sys
from MovieTheaterSeating import MovieTheater


if __name__ == "__main__":
	input_file = open(sys.argv[1], 'r')
	output_file = open("output.txt", "w")
	rows = 10
	seats = 20
	theater = MovieTheater(rows,seats)
	for reservation in input_file:
		output = theater.book(reservation)
		if output != None:
			output_file.write(output)

	input_file.close()
	output_file.close()
	print("Your outfile is saved in output.txt")