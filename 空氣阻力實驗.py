speed = 0
mass = 10
affected_area = 10
x = 0
min_time = 0.01

all_position = []
all_speed = []


#F=(1/2)CρSV^2
#x = vot + 1/2at^2

def drag_force(current_speed, affected_area, drag_coefficient = 0.4, air_density = 1.225):
    print("drag_force:", drag_coefficient * air_density * affected_area * current_speed * current_speed / 2)
    return drag_coefficient * air_density * affected_area * current_speed * current_speed / 2

def gravity_force(mass, gravity = 9.8):
    print("gravity_force:", mass * gravity)
    return mass * gravity

def final_acceleration(gravity_force, drag_force, mass):
    print("final_acceleration:", (gravity_force - drag_force) / mass)
    return (gravity_force - drag_force) / mass

def delta_time_move(acceleration, min_time, current_speed):
    print("delta_time_move:", current_speed * min_time + acceleration * min_time * min_time / 2)
    return current_speed * min_time + acceleration * min_time * min_time / 2

def delta_time_speed(acceleration, min_time, current_speed):
    print("delta_time_speed:", current_speed + acceleration * min_time)
    return current_speed + acceleration * min_time

for i in range(500):
    x += delta_time_move(final_acceleration(gravity_force(mass), drag_force(speed, affected_area), mass), min_time, speed)
    speed += delta_time_speed(final_acceleration(gravity_force(mass), drag_force(speed, affected_area), mass), min_time, speed)
    print()
    print("--------------------------------------------")
    print(">>> now position <<<", x)
    print(">>> now speed <<<", speed)
    print("--------------------------------------------")
    print()
    all_position.append(x)
    all_position.append(speed)

#print(all_position)
#print(all_speed)
