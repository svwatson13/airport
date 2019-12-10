from airport_classes import *
import pytest

## SETUP

passenger1 = Passengers('Sam', 2321)
passenger2 = Passengers('John', 2345)

## ASSERTIONS

# Test where method of class and after comma is what appears if test fails
def test_passname():
    assert passenger1.name == 'Sam', 'Passenger 1 was not created'
    assert passenger2.name == 'John', 'Passenger 2 is not called Dave'

def test_passPN():
    assert passenger1.passnum == 2321, 'Passnumber not created'
    assert passenger2.passnum == 2345, 'Passnumber incorrect'

# Testing whether error 'TypeError' is produced when not enough arguments are passed into a class
def test_error():
    with pytest.raises(TypeError):
        Passengers('Sam')

def test_plane():
    new_plane = Planes('Bertha', 1234)
    assert new_plane.planenum == 1234
    assert new_plane.name == 'Bertha'

def test_flight_creation():
    new_flight = Flight()
    # Testing that new_flight is a Flight object
    assert isinstance(new_flight, Flight)

def test_adding_details():
    new_flight = Flight('Bertha', 'Kansas', 'London', 9871)
    assert new_flight.name == 'Bertha'
    assert new_flight.origin == 'Kansas'
    assert new_flight.destination == 'London'

def test_passenger_list():
    new_flight = Flight('Bertha', 'Kansas', 'London', 9871)
    new_flight.add_passengers('Sam') == 'Sam'
    assert isinstance(passengers, list)
    assert passengers[0] == 'Sam'




