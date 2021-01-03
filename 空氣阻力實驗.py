import matplotlib.pyplot as plt

all_position = []
all_speed = []

all_position_2 = []
all_speed_2 = []

all_position_3 = []
all_speed_3 = []

#F=(1/2)CρSV^2
#x = vot + 1/2at^2

min_time = 0.001
data_count = 3000

#初始化
speed = 0
x = 0
#可調整
mass = 10
affected_area = 0



def drag_force(current_speed, affected_area, drag_coefficient = 0.4, air_density = 1.225):
    #print("drag_force:", drag_coefficient * air_density * affected_area * current_speed * current_speed / 2)
    try:
        return drag_coefficient * air_density * affected_area * current_speed * current_speed / 2
    except ZeroDivisionError:
        return 0
    
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

for i in range(data_count):
    x += delta_time_move(final_acceleration(gravity_force(mass), drag_force(speed, affected_area), mass), min_time, speed)
    speed = delta_time_speed(final_acceleration(gravity_force(mass), drag_force(speed, affected_area), mass), min_time, speed)
    #print(delta_time_speed(final_acceleration(gravity_force(mass), drag_force(speed, affected_area), mass), min_time, speed))
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
mass2 = 200
affected_area2 = 100


for i in range(data_count):
    x2 += delta_time_move(final_acceleration(gravity_force(mass2), drag_force(speed2, affected_area2), mass2), min_time, speed2)
    speed2 = delta_time_speed(final_acceleration(gravity_force(mass2), drag_force(speed2, affected_area2), mass2), min_time, speed2)
    #print()
    #print("--------------------------------------------")
    #print(">>> now position <<<", x2)
    #print(">>> now speed <<<", speed2)
    #print("--------------------------------------------")
    #print()
    all_position_2.append(x2)
    all_speed_2.append(speed2)

#初始化
speed3 = 0
x3 = 0
#可調整
mass3 = 200
affected_area3 = 200


for i in range(data_count):
    x3 += delta_time_move(final_acceleration(gravity_force(mass3), drag_force(speed3, affected_area3), mass3), min_time, speed3)
    speed3 = delta_time_speed(final_acceleration(gravity_force(mass3), drag_force(speed3, affected_area3), mass3), min_time, speed3)
    #print()
    #print("--------------------------------------------")
    #print(">>> now position <<<", x3)
    #print(">>> now speed <<<", speed3)
    #print("--------------------------------------------")
    #print()
    all_position_3.append(x3)
    all_speed_3.append(speed3)

plt.subplot(1, 2, 1)
posLine1 = plt.plot(all_position, label="S = " + str(affected_area))
posLine2 = plt.plot(all_position_2, label="S = " + str(affected_area2))
posLine3 = plt.plot(all_position_3, label="S = " + str(affected_area3))
plt.legend(loc='best')
plt.title("x-t graph", fontsize = 24)
plt.xlabel("Time (1 = " + str(min_time) + "sec)", fontsize = 16)
plt.ylabel("x", fontsize = 16)
plt.tick_params(axis='both', labelsize = 12, color='red')

plt.subplot(1, 2, 2)
plt.title("v-t graph", fontsize = 24)
plt.xlabel("Time (1 = " + str(min_time) + "sec)", fontsize = 16)
plt.ylabel("v", fontsize = 16)
posLine1 = plt.plot(all_speed, label="S = " + str(affected_area))
posLine2 = plt.plot(all_speed_2, label="S = " + str(affected_area2))
posLine3 = plt.plot(all_speed_3, label="S = " + str(affected_area3))
plt.legend(loc='best')
plt.tick_params(axis='both', labelsize = 12, color='red')

plt.show()


