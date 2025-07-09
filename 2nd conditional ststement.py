light = input("Enter the traffic light color (green, yellow, red): ").lower()
if(light == "green"):
    print("You can go")
elif(light == "yellow"):
    print("You should slow down")
elif(light == "red"):
    print("You should stop")
else:
    print("light is broken")
