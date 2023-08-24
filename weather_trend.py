#weather data source: https://www.wunderground.com/history/monthly/us/ca/mountain-view/KSJC
import matplotlib.pyplot as plt

FILE_PATH = 'mtv_weather_May.csv'
def main():
    file = open(FILE_PATH)
    day = []
    temp_max = []
    temp_min = []
    avg_temp = []
    for line in file:
        line = line.strip()
        parts = line.split(',')
        day.append(parts[0])
        temp_max.append(parts[1])
        temp_min.append(parts[3])
        avg_temp.append(parts[2])
    day.pop(0)
    temp_max.pop(0)
    temp_max = list(map(float,temp_max))
    temp_min.pop(0)
    temp_min = list(map(float,temp_min))
    avg_temp.pop(0)
    avg_temp = list(map(float,avg_temp))

    print('day:',day)
    print('Max:',temp_max)
    print('Min:',temp_min)
    print('Avg:',avg_temp)
    fig, ax = plt.subplots()
    ax.plot(day, temp_max, label="High temperature")
    ax.plot(day, temp_min, label="Low temperature")
    ax.plot(day, avg_temp, label='Average temperature')


    ax.legend()
    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.show()
if __name__ == '__main__':
    main()



