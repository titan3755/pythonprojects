import random as rnd
import colorama as cc
import time as t
import functions

speed = 0
status = 'ok'
running = True
while running:
    response = input('>')
    if response.lower() == 'help':
        print(f"""
All available commands -->
    start - starts the car
    quit - ends the program
    status - status of the car
Commands after starting car -->
    status - Status of the car
    accelerate - Increases the speed by 10 Kmph
    brake - Decreases the speed by 10 Kmph
    random ac - Increases the speed by a random factor
    random br - Decreases the speed by a random factor
    force ac - Forcibly increases the speed ignoring speed limit but may damage car
    stop - Stops the car
    
        """)
    elif response.lower() == 'status':
        print('Status: ' + status)
    elif response.lower() == 'quit':
        break
    elif response.lower() == 'start':
        if status == 'ok' or status == 'damaged':
            print('Starting Car ...')
            t.sleep(1.5)
            start_car = True
            print('Car Started!')
        else:
            print('Car too damaged to be started!')
        while start_car and status == 'ok' or status == 'damaged':
            start_responses = input('>')
            if start_responses.lower() == 'accelerate':
                speed_code = functions.speed_checker(speed)
                if speed_code == 0:
                    speed += 10
                    print('Accelerating ...')
                    t.sleep(1)
                    print('Speed increased by 10 Kmph' + '\nTotal speed: ' + str(speed) + ' Kmph')
                elif speed_code == 1:
                    speed -= 20
                    print('Speed too high! Slowed down by 20 Kmph' + '\nTotal speed: ' + str(speed) + ' Kmph')
                else:
                    speed = 0
                    print('Something has gone wrong!')
            elif start_responses.lower() == 'brake':
                if speed == 0:
                    print("The car is stationary already!")
                elif speed >= 10:
                    speed -= 10
                    print('Braking ...')
                    t.sleep(1.5)
                    print('Speed reduced by 10 Kmph!\nTotal speed: ' + str(speed) + 'Kmph')
                elif speed < 10:
                    print('Speed too low to brake! Accelerate first')
                elif speed < 0:
                    speed = 0
                    print('The car is stationary already!')
                else:
                    speed = 0
                    print('Something has gone wrong!')
            elif start_responses.lower() == 'stop':
                speed = 0
                print('Stopping car ...')
                t.sleep(1)
                print('Car stopped!')
                break
            elif start_responses.lower() == 'random ac':
                random_factor = rnd.randint(1, 25)
                speed_value = functions.speed_checker(speed)
                if speed_value == 0:
                    speed += random_factor
                    print('Accelerating ...')
                    t.sleep(1)
                    print('Speed increased by ' + str(random_factor) + 'Kmph.\nTotal speed: ' + str(speed) + 'Kmph')
                elif speed_value == 1:
                    speed -= random_factor
                    print('Speed limit broken! Speed reduced by ' + str(random_factor) + 'Kmph.\nTotal speed: ' + str(speed))
                else:
                    speed = 0
                    print('Something has gone wrong!')
            elif start_responses.lower() == 'random br':
                random_brake = rnd.randint(1, 25)
                if speed == 0:
                    print("The car is stationary already!")
                elif speed >= random_brake:
                    speed -= random_brake
                    print('Braking ...')
                    t.sleep(1.5)
                    print('Speed reduced by ' + str(random_brake) + 'Kmph.\nTotal speed: ' + str(speed) + 'Kmph')
                elif speed < random_brake:
                    print('Speed too low to brake! Accelerate first')
                elif speed < 0:
                    speed = 0
                    print('The car is stationary already!')
                else:
                    speed = 0
                    print('Something has gone wrong!')
            elif start_responses.lower() == 'force ac':
                force_ac_factor = rnd.randint(45, 55)
                speed_check = functions.speed_checker(speed)
                if speed_check == 0:
                    speed += force_ac_factor
                    print('Force Accelerating ...')
                    t.sleep(3)
                    print('Speed increased by ' + str(force_ac_factor) + 'Kmph.\nTotal speed: ' + str(speed) + 'Kmph')
                elif speed_check == 1:
                    speed += force_ac_factor
                    status = 'damaged'
                    print('Speed limit crossed but accelerating ...')
                    t.sleep(2)
                    print('Car has been damaged!\nSpeed increased by ' + str(force_ac_factor) + 'Kmph.\nTotal speed: ' + str(speed) + 'Kmph')
                else:
                    speed = 0
                    status = 'ok'
                    print('Something went wrong!')

