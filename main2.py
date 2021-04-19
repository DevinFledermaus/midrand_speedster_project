# SPEEDING
speed_limit = int(input("What is the speed limit: "))
driver_speed = int(input("What is your speed: "))
Points = 0

if driver_speed <= speed_limit:
    print("OK")
else:
    while driver_speed > speed_limit:
        driver_speed -= 5
        Points += 1
if Points > 12:
    print("Time to go to jail")
print("Points: "+str(Points))
