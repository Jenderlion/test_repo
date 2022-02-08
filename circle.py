import matplotlib.pyplot as plt
import math

n = int(input('Угол исследуемой части окружности: '))
while n >= 360:
    n -= 360

x_param = []
y_param = []
for i in range(0, 361):
    y_param.append(math.cos(math.radians(i)))
    x_param.append(math.sin(math.radians(i)))

x_angle = [0, math.cos(math.radians(n))]
y_angle = [0, math.sin(math.radians(n))]

for i in range(n, -1, -1):
    x_angle.append(math.cos(math.radians(i)))
    y_angle.append(math.sin(math.radians(i)))

x_angle.append(0)
y_angle.append(0)

fig, ax = plt.subplots(figsize=(5, 5), num='Circle!')
ax.plot(x_param, y_param)
ax.plot(x_angle, y_angle)
x_horde = [x_angle[1], x_angle[-2]]
y_horde = [y_angle[1], y_angle[-2]]
ax.plot(x_horde, y_horde)

horde_length = 2 * math.sin(math.radians(float(n)/2))
plt.text(-1, 1.15, f'Длина хорды: {round(horde_length, 3)} * R'
                   f'\nДлина дуги: {round(math.radians(n), 3)} rad'
                   f'\nS = {round(math.pi*(n/360), 3)} * R^2')

plt.grid()
plt.show()

print(x_angle)
print(y_angle)
