import screen_brightness_control as sbc

print("____________Welcome to your Desktop Brightness Adjustment App_______________")

# get current brightness
print("Current Brightness in your PC is: ")
print(sbc.get_brightness())


# Go into the Adjustment Loop
st = input("Do you want to Adjust your Brightness? [y/n]?")
if st=='Y' or st=='y':
    adjLoop = True
elif st=='N' or st=='n':
    adjLoop = False
else:
    print("You Entered Wrong Input. App will be Closed..!")
    adjLoop == False

while(adjLoop):
    level = input("Enter Brightness Level you want: ")
    sbc.set_brightness(level)

    print("Your Current Brightness Level is: ")
    print(sbc.get_brightness())

    print("Do you want to Adjust Brightness? [y/n]?")
    inp = input()
    if inp=='Y' or inp=='y':
        run = True
    elif inp=='N' or inp=='n':
        run = False
    else:
        print("You Entered wrong input. It will Terminate..!")
        run = False
    if not run:
        break
