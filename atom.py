from vpython import *

scene2 = canvas(width=500,height=500,background = vector(1,1,1))

# Определение констант

pi = 2*asin(1.0)                      # Определение значения пи с помощью sin (pi / 2) = 1
a0 = 0.529177e-10                     # Радиус первой орбиты
m_p = 1.6726219e-27                   # Масса протона
m_e = 9.10938356e-31                  # Масса электрона
e = 1.6021765e-19                     # Заряд электрона
epsilon = 8.854187e-12
v_e = e/sqrt(4*pi*epsilon*a0*m_e)     # Формула: mv^2/r = e^2/(4*pi*epsilon*r^2)
c = 3e8
print("Радиус первой орбиты = ",a0, " м")
print("Скорость электрона на первой орбите = ", v_e, " м/с")

#Определение 3D-объектов

nucleus = sphere(pos = vector(0,0,0), radius = 0.1*a0, velocity = vector(0,0,0), mass = m_p, charge = e, color = color.yellow)
electron = sphere(pos = vector(1.4*a0,0,0), radius = 0.02*a0, velocity = vector(0,v_e,0), mass = m_e, charge = -e, color = color.red)
electron.trail=curve(color=electron.color)

#Определение функции для расчета ускорения

def acc():
  dr = electron.pos - nucleus.pos
  Force = 1./(4.*pi*epsilon)*nucleus.charge*electron.charge/(mag(dr)**2) * norm(dr)
  m1 = electron.mass
  return Force/m1

#Определение порядка времени и временного шага

t = 0
T_orbit = 2.*pi*a0/v_e
t_end = 1000*T_orbit
dt = T_orbit/1000.
print("Период времени на первой орбите= ",T_orbit, " с")

# Обновление положения электрона в цикле

while (t<t_end):
  rate(100)
  electron.velocity = electron.velocity + acc()*dt
  electron.pos = electron.pos + electron.velocity*dt
  electron.trail.append(pos = electron.pos)
  t = t+dt
