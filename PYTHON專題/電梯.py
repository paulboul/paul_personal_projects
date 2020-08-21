from time import sleep

current_floor=5


while True:
    target_floor=input("now you are in the"+str(current_floor)+"floor.which floor are you going?\n>>")
    
    try:
        target_floor=int(target_floor)
    except ValueError:
        print("wrong,please input the number\n")
        continue
    if target_floor < 1 or target_floor > 7:
        print("please input in 1-7 numbers\n")
        continue
    if target_floor==current_floor:
        continue
    
    elif target_floor<current_floor:
        print("The evealtor down")
        while target_floor<current_floor:
            print(current_floor)
            current_floor=current_floor-1
            sleep(0.5)
        print(current_floor)
        
    else:
        print("The evaltor up")
        while target_floor>current_floor:
            print(current_floor)
            current_floor=current_floor+1
            sleep(0.5)
        print(current_floor)        