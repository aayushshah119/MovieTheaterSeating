#This class defines a particular row in the Movie Theater. Seat_pointer points to the
# seat that can be filled by the program. Empty seats is the number of empty seats in
# this row. Id is from the list {A,B,C,...,J}
class Row:
	def __init__(self, seats, id):
		self.seat_pointer = 1
		self.emptyseats = seats
		self.id = chr(64 + id)


# This class defines the Movie Theater. Seating is a list of row objects. Row pointer 
# ranges from [1,10] and corresponds to the letters [J,A]
class MovieTheater:
	def __init__(self,rows,seats):
		self.rows = rows
		self.seats = seats
		self.seating = [Row(seats, 10-i) for i in range(rows)]
		self.row_pointer = rows

	#This methods updates our seating arrangement and returns the assigned seats
	def book(self, reservation):
		bookings = []
		user_input = reservation.split()
		reservationId = user_input[0]
		number_of_seats = int(user_input[1])

		if (number_of_seats > self.get_empty_seats()):
			print("Not enough seats for " + reservationId)
			return

		row = self.best_row(number_of_seats)

		#If all seats can be assigned in one row, then row will be assigned. None otherwise
		if row != None:
			for i in range(number_of_seats):
				seat_number = chr(64 + self.row_pointer) + str(row.seat_pointer)
				bookings.append(seat_number)
				row.seat_pointer += 1
				row.emptyseats -= 1

		# If all seats can't be assigned in one row, we break the group. 
		# Assign as many seats as possible starting from the top most row.
		else:
			self.row_pointer = self.rows
			counter = 0
			for item in self.seating:
				while ((item.emptyseats != 0) & (counter < number_of_seats)):
					seat_number = chr(64 + self.row_pointer) + str(item.seat_pointer)
					bookings.append(seat_number)
					item.seat_pointer += 1
					item.emptyseats -= 1

					counter += 1

				if counter < number_of_seats:
					self.row_pointer -= 1
				else:
					row = item
					break

		delimeter = ","
		bookings = " ".join([reservationId,delimeter.join(bookings)]) + "\n"
		
		self.ensure_safety(row)
		return bookings

	# This methods creates a buffer of 3 seats to ensure customer safety
	def ensure_safety(self, row):
		buffer = 3
		for i in range(buffer):
			row.seat_pointer += 1
			row.emptyseats -= 1
		if (row.emptyseats <= 0):
			row.emptyseats = 0


	# This methods returns the best row to maximize customer satisfaction. ...
	def best_row(self, number_of_seats):
		row_number = self.rows
		for row in self.seating:
			if number_of_seats <= row.emptyseats:
				self.row_pointer = row_number
				return row
			row_number -= 1
		return None

	# Returns the total number of emtpy seats in the movie theater
	def get_empty_seats(self):
		empty = 0
		for row in self.seating:
			empty += row.emptyseats
		return empty