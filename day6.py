from utils import cache_and_read_input


input = cache_and_read_input(6)

data = input.split('\n')[1:-1]

wins = []

time = ''
record = ''

for race in data:
    components = race.split()
    time += str(components[0])
    record += str(components[1])
time = int(time)
record = int(record)
speed = 0
distance = 0

winning_times = 0

while time > 0:
    speed += 1
    time -= 1
    distance = speed * time
    if distance > record:
        winning_times += 1

wins.append(winning_times)

print(wins)
print(36*23*9*37)

