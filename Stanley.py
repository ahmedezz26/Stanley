import math
pi =3.141592654
def stanley(Velocity,Gain,error):
    car_Velocity = Velocity
    trackError = error
    Gain_S =Gain
    if error <= 5:
     steeringAngle = math.atan((Gain_S * trackError)/car_Velocity)

    elif trackError > 5:
     steeringAngle = math.atan((Gain_S * trackError)/car_Velocity) + pi/2
    print("the steering angle(rad)= ",steeringAngle)
    print("the steering angle(degrees)=  ",math.degrees(steeringAngle))

Vel = input("Enter the Velocity: ")
gain = input("Enter the Gain: ")
err = input("Enter the error: ")
Vel = int(Vel)
gain = int(gain)
err = int(err)
stanley(Vel,gain,err)
