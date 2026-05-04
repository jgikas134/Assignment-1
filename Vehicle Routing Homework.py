# Input: getting time and speed
timeHours = float(input("Enter total travel time in hours: "))
speedMPH = float(input("Enter average speed in miles per hour: "))

# Distance
distance = timeHours * speedMPH
print(f"Distance travelled: {distance:.2f} miles")

# Route data
localDistance = 1.00 * 30
parkwayDistance = 0.88 * 40
highwayDistance = 0.87 * 55

print(f"Local route distance: {localDistance:.2f} miles")
print(f"Parkway route distance: {parkwayDistance:.2f} miles")
print(f"Highway route distance: {highwayDistance:.2f} miles")

# Finding the shortest route
shortest = min(localDistance, parkwayDistance, highwayDistance)

if shortest == localDistance:
    print("Shortest route: Local")
elif shortest == parkwayDistance:
    print("Shortest route: Parkway")
else:
    print("Shortest route: Highway")