# SPEEDING
speed_limit = int(input("What is the speed limit: "))
driver_speed = int(input("What is your speed: "))

if driver_speed <= speed_limit:
    print("OK")
elif driver_speed >= speed_limit + 5 and (driver_speed <= speed_limit + 9):
    print("Points: 1")
elif driver_speed >= speed_limit + 10 and (driver_speed <= speed_limit + 14):
    print("Points: 2")
elif driver_speed >= speed_limit + 15 and (driver_speed <= speed_limit + 19):
    print("Points: 3")
elif driver_speed >= speed_limit + 20 and (driver_speed <= speed_limit + 24):
    print("Points: 4")
elif driver_speed >= speed_limit + 25 and (driver_speed <= speed_limit + 29):
    print("Points: 5")
elif driver_speed >= speed_limit + 30 and (driver_speed <= speed_limit + 34):
    print("Points: 6")
elif driver_speed >= speed_limit + 35 and (driver_speed <= speed_limit + 39):
    print("Points: 7")
elif driver_speed >= speed_limit + 40 and (driver_speed <= speed_limit + 44):
    print("Points: 8")
elif driver_speed >= speed_limit + 45 and (driver_speed <= speed_limit + 49):
    print("Points: 9")
elif driver_speed >= speed_limit + 50 and (driver_speed <= speed_limit + 54):
    print("Points: 10")
elif driver_speed >= speed_limit + 55 and (driver_speed <= speed_limit + 59):
    print("Points: 11")
elif driver_speed >= speed_limit + 60 and (driver_speed <= speed_limit + 64):
    print("Points: 12")
elif driver_speed >= speed_limit + 65:
    print("Time to go to Jail")
