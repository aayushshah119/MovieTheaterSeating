import pytest
import filecmp
from MovieTheaterSeating import MovieTheater

rows = 10
seats = 20

def test_simple_insertion():
  """ Tests a simple insertion in the same row """
  instructions = ["R0001 2", "R0002 8"]
  output = ["R0001 J1,J2", "R0002 J6,J7,J8,J9,J10,J11,J12,J13"]
  theater = MovieTheater(rows, seats)
  for i in range(len(instructions)):
    reservation_request = instructions[i]
    result = theater.book(reservation_request).strip()
    assert output[i] == result

def test_split_group():
  """ Tests reservations resulting in different row due to space constraint in one row"""
  instructions = ["R0001 10", "R0002 8"]
  output = ["R0001 J1,J2,J3,J4,J5,J6,J7,J8,J9,J10", "R0002 I1,I2,I3,I4,I5,I6,I7,I8"]
  theater = MovieTheater(rows, seats)
  for i in range(len(instructions)):
    reservation_request = instructions[i]
    result = theater.book(reservation_request).strip()
    assert output[i] == result

def test_safety():
  """Tests if seats are left for customer safety"""
  instructions = ["R0001 10", "R0002 8", "R0003 1", "R0004 3"]
  output = ["R0001 J1,J2,J3,J4,J5,J6,J7,J8,J9,J10", "R0002 I1,I2,I3,I4,I5,I6,I7,I8", 
            "R0003 J14", "R0004 J18,J19,J20"]
  theater = MovieTheater(rows, seats)
  for i in range(len(instructions)):
    reservation_request = instructions[i]
    result = theater.book(reservation_request).strip()
    assert output[i] == result


def test_full_insertion():
  instructions = ["R0001 18", "R0002 17","R0003 6","R0004 10", "R0005 5","R0006 17",
                "R0007 5", "R0008 8", "R0009 11","R0010 9","R0011 3","R0012 13",
                "R0013 9", "R0014 9", "R0015 7", "R0016 3", "R0017 4", "R0018 8"]
  output = ["R0001 J1,J2,J3,J4,J5,J6,J7,J8,J9,J10,J11,J12,J13,J14,J15,J16,J17,J18",
          "R0002 I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13,I14,I15,I16,I17",
          "R0003 H1,H2,H3,H4,H5,H6",
          "R0004 H10,H11,H12,H13,H14,H15,H16,H17,H18,H19",
          "R0005 G1,G2,G3,G4,G5", 
          "R0006 F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17",
          "R0007 G9,G10,G11,G12,G13", 
          "R0008 E1,E2,E3,E4,E5,E6,E7,E8", 
          "R0009 D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11", 
          "R0010 E12,E13,E14,E15,E16,E17,E18,E19,E20", 
          "R0011 G17,G18,G19", 
          "R0012 C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13", 
          "R0013 B1,B2,B3,B4,B5,B6,B7,B8,B9",
          "R0014 A1,A2,A3,A4,A5,A6,A7,A8,A9", 
          "R0015 B13,B14,B15,B16,B17,B18,B19", 
          "R0016 D15,D16,D17", 
          "R0017 C17,C18,C19,C20",
          "R0018 A13,A14,A15,A16,A17,A18,A19,A20"]

  theater = MovieTheater(rows, seats)
  for i in range(len(instructions)):
    if output[i] == None:
      assert output[i] == theater.book(instructions[i])
      break
    reservation_request = instructions[i]
    result = theater.book(reservation_request).strip()
    assert output[i] == result

def test_missing_reservation():
  instructions = ["R0001 18", "R0002 17","R0003 6","R0004 10", "R0005 5","R0006 17",
                "R0007 5", "R0008 8", "R0009 11","R0010 9","R0011 3","R0012 13",
                "R0013 9", "R0014 9", "R0015 7", "R0016 3", "R0017 4", "R0018 9",
                "R0019 8"]
  output = ["R0001 J1,J2,J3,J4,J5,J6,J7,J8,J9,J10,J11,J12,J13,J14,J15,J16,J17,J18",
          "R0002 I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13,I14,I15,I16,I17",
          "R0003 H1,H2,H3,H4,H5,H6",
          "R0004 H10,H11,H12,H13,H14,H15,H16,H17,H18,H19",
          "R0005 G1,G2,G3,G4,G5", 
          "R0006 F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17",
          "R0007 G9,G10,G11,G12,G13", 
          "R0008 E1,E2,E3,E4,E5,E6,E7,E8", 
          "R0009 D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11", 
          "R0010 E12,E13,E14,E15,E16,E17,E18,E19,E20", 
          "R0011 G17,G18,G19", 
          "R0012 C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13", 
          "R0013 B1,B2,B3,B4,B5,B6,B7,B8,B9",
          "R0014 A1,A2,A3,A4,A5,A6,A7,A8,A9", 
          "R0015 B13,B14,B15,B16,B17,B18,B19", 
          "R0016 D15,D16,D17", 
          "R0017 C17,C18,C19,C20", 
          None,
          "R0019 A13,A14,A15,A16,A17,A18,A19,A20"]

  theater = MovieTheater(rows, seats)
  for i in range(len(instructions)):
    if output[i] == None:
      assert output[i] == theater.book(instructions[i])
      break
    reservation_request = instructions[i]
    result = theater.book(reservation_request).strip()
    assert output[i] == result

def test_random():
  instructions = ["R0001 8","R0002 8","R0003 9","R0004 7","R0005 11","R0006 13", "R0007 12",
                "R0008 1", "R0009 5", "R0010 19", "R0011 2", "R0012 1", "R0013 17", "R0014 5",
                "R0015 5", "R0016 7", "R0017 4", "R0018 6", "R0019 19", "R0020 3", "R0021 4",
                "R0022 3", "R0023 1"]
  output = ["R0001 J1,J2,J3,J4,J5,J6,J7,J8",
            "R0002 J12,J13,J14,J15,J16,J17,J18,J19",
            "R0003 I1,I2,I3,I4,I5,I6,I7,I8,I9",
            "R0004 I13,I14,I15,I16,I17,I18,I19",
            "R0005 H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,H11",
            "R0006 G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,G12,G13",
            "R0007 F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12",
            "R0008 H15",
            "R0009 F16,F17,F18,F19,F20",
            "R0010 E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19",
            "R0011 H19,H20",
            "R0012 G17",
            "R0013 D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17",
            "R0014 C1,C2,C3,C4,C5",
            "R0015 C9,C10,C11,C12,C13",
            "R0016 B1,B2,B3,B4,B5,B6,B7",
            "R0017 C17,C18,C19,C20",
            "R0018 B11,B12,B13,B14,B15,B16",
            "R0019 A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19",
            None,
            None,
            None,
            "R0023 B20"]
  theater = MovieTheater(rows, seats)
  for i in range(len(instructions)):
    if output[i] == None:

      assert output[i] == theater.book(instructions[i])
      break
    reservation_request = instructions[i]
    result = theater.book(reservation_request).strip()
    assert output[i] == result

def test_change_parameters():
  rows = 2
  seats = 5
  instructions = ["R0001 1", "R0002 2", "R0003 1"]
  output = ["R0001 B1", "R0002 A1,A2", "R0003 B5"]
  theater = MovieTheater(rows, seats)
  for i in range(len(instructions)):
    if output[i] == None:
      assert output[i] == theater.book(instructions[i])
      break
    reservation_request = instructions[i]
    result = theater.book(reservation_request).strip()
    assert output[i] == result

def test_get_empty_seats():
  theater = MovieTheater(rows,seats)
  instructions = ["R0001 10", "R0002 10", "R0003 10", "R0004 10", "R0005 10", "R0006 10", "R0007 10",
                  "R0008 10", "R0009 10", "R0010 10"]
  for i in range(len(instructions)):
    reservation_request = instructions[i]
    result = theater.book(reservation_request).strip()
  assert theater.get_empty_seats() == 70


def test_best_row():
  theater = MovieTheater(rows, seats)
  instructions = ["R0001 10", "R0002 8"]
  result = theater.book(instructions[0]).strip()
  best_row = theater.best_row(8)
  output_row = theater.seating[1]
  assert best_row.id == output_row.id


def test_best_row_complex():
  theater = MovieTheater(rows, seats)
  instructions = ["R0001 10", "R0002 10", "R0003 10", "R0004 10", "R0005 10", "R0006 10", "R0007 10",
                  "R0008 10", "R0009 10", "R0010 10"]
  for i in range(len(instructions)):
    reservation_request = instructions[i]
    result = theater.book(reservation_request).strip()
  best_row = theater.best_row(1)
  output_row = theater.seating[0]
  assert best_row.id == output_row.id


def test_best_row_none():
  theater = MovieTheater(rows, seats)
  instructions = ["R0001 10", "R0002 10", "R0003 10", "R0004 10", "R0005 10", "R0006 10", "R0007 10",
                  "R0008 10", "R0009 10", "R0010 10"]
  for i in range(len(instructions)):
    reservation_request = instructions[i]
    result = theater.book(reservation_request).strip()
  best_row = theater.best_row(10)
  assert best_row == None