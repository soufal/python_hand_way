#the num of cars
cars = 100

#the space of a car
space_in_a_car = 4.0

#the num of drivers
drivers = 30

#the num of passengers
passengers = 90

#the num of cars are not driven
cars_not_driven = cars - drivers

#the num of cars are driven
cars_driven = drivers

#the carpool capacity
carpool_capacity = cars_driven * space_in_a_car

#average of passengers for per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")