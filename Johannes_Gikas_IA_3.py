# Problem 1
# get sales
while True:
    try:
        target = float(input("Enter total sales target: "))
        if target > 0:
            break
        else:
            print("Invalid input")
    except:
        print("Invalid input")

total = 0.0

for day in range(1, 6):

    while True:
        try:
            sales = float(input("Enter day " + str(day) + " sales: "))
            if sales > 0:
                break
            else:
                print("Invalid input")
        except:
            print("Invalid input")

    total = total + sales
    percent = (total / target) * 100
    print("Cumulative sales:", total, "(", percent, "% )")

print()

# Problem 2
route = 1
fastest_time = 0
fastest_route = 0

while True:

    while True:
        try:
            distance = float(input("Enter route " + str(route) + " distance (miles): "))
            if distance > 0:
                break
            else:
                print("Invalid input")
        except:
            print("Invalid input")

    while True:
        try:
            speed = float(input("Enter route " + str(route) + " speed (miles/hour): "))
            if speed > 0:
                break
            else:
                print("Invalid input")
        except:
            print("Invalid input")

    time = (distance / speed) * 60
    print("Route", route, "time:", round(time), "minutes")

    if fastest_route == 0 or time < fastest_time:
        fastest_time = time
        fastest_route = route

    more = input("More routes (y/n)?: ")

    if more == "n":
        break

    route = route + 1

print("Route", fastest_route, "is fastest;", round(fastest_time), "minutes")