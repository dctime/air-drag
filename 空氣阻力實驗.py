import matplotlib.pyplot as plt

all_position = []
all_speed = []

all_position_2 = []
all_speed_2 = []
#F=(1/2)CρSV^2
#x = vot + 1/2at^2

min_time = 0.01

#初始化
speed = 0
x = 0
#可調整
mass = 10
affected_area = 100



def drag_force(current_speed, affected_area, drag_coefficient = 0.4, air_density = 1.225):
    #print("drag_force:", drag_coefficient * air_density * affected_area * current_speed * current_speed / 2)
    return drag_coefficient * air_density * affected_area * current_speed * current_speed / 2

def gravity_force(mass, gravity = 9.8):
    #print("gravity_force:", mass * gravity)
    return mass * gravity

def final_acceleration(gravity_force, drag_force, mass):
    #print("final_acceleration:", (gravity_force - drag_force) / mass)
    return (gravity_force - drag_force) / mass

def delta_time_move(acceleration, min_time, current_speed):
    #print("delta_time_move:", current_speed * min_time + acceleration * min_time * min_time / 2)
    return current_speed * min_time + acceleration * min_time * min_time / 2

def delta_time_speed(acceleration, min_time, current_speed):
    #print("delta_time_speed:", current_speed + acceleration * min_time)
    return current_speed + acceleration * min_time

for i in range(100):
    x += delta_time_move(final_acceleration(gravity_force(mass), drag_force(speed, affected_area), mass), min_time, speed)
    speed += delta_time_speed(final_acceleration(gravity_force(mass), drag_force(speed, affected_area), mass), min_time, speed)
    #print()
    #print("--------------------------------------------")
    #print(">>> now position <<<", x)
    #print(">>> now speed <<<", speed)
    #print("--------------------------------------------")
    #print()
    all_position.append(x)
    all_speed.append(speed)

#print(all_position)
#print(all_speed)

#初始化
speed2 = 0
x2 = 0
#可調整
mass2 = 10
affected_area2 = 200


for i in range(100):
    x2 += delta_time_move(final_acceleration(gravity_force(mass2), drag_force(speed2, affected_area2), mass2), min_time, speed2)
    speed2 += delta_time_speed(final_acceleration(gravity_force(mass2), drag_force(speed2, affected_area2), mass2), min_time, speed2)
    #print()
    #print("--------------------------------------------")
    #print(">>> now position <<<", x2)
    #print(">>> now speed <<<", speed2)
    #print("--------------------------------------------")
    #print()
    all_position_2.append(x2)
    all_speed_2.append(speed2)

plt.subplot(2, 1, 1)
plt.plot(all_position)
plt.plot(all_position_2)
plt.tick_params(axis='both', labelsize = 12, color='red')

plt.subplot(2, 1, 2)
plt.plot(all_speed)
plt.plot(all_speed_2)
plt.tick_params(axis='both', labelsize = 12, color='red')

plt.show()


