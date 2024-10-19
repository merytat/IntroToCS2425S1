#input
distance = float(input("Enter distance (m): "))
time = float(input("Enter time (s): "))

#process
velocity = distance / time

#output
print("Velocity is: ", round(velocity,2), "m/s")