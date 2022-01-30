import matplotlib.pyplot as plt
import json

d1 = json.load(open('data_50.json', 'r'))
d2 = json.load(open('data_100.json', 'r'))
d3 = json.load(open('data_500.json', 'r'))
d4 = json.load(open('data_1000.json', 'r'))
d5 = json.load(open('data_5000.json', 'r'))

l = [d1, d2, d3, d4, d5]

# Visited
xAxis = [ 50, 100, 500, 1000, 5000]
yAxis = [ sub['visited'] for sub in l ]
plt.grid(True)
plt.plot(xAxis,yAxis, color='maroon', marker='o')
plt.xlabel('No. of links')
plt.ylabel('Visited')
plt.show()

# To visit
xAxis = [ 50, 100, 500, 1000, 5000]
yAxis = [ sub['to_visit'] for sub in l ]
plt.grid(True)
plt.plot(xAxis,yAxis, color='maroon', marker='o')
plt.xlabel('No. of links')
plt.ylabel('To Visit')
plt.show()

# Ratio of visited / to visit
xAxis = [ 50, 100, 500, 1000, 5000]
yAxis = [ sub['visited'] / sub['to_visit'] for sub in l ]
plt.grid(True)
plt.plot(xAxis,yAxis, color='maroon', marker='o')
plt.xlabel('No. of links')
plt.ylabel('Visited / To Visit')
plt.show()

# Time taken
xAxis = [ 50, 100, 500, 1000, 5000]
yAxis = [ sub['elapsed_time_seconds'] for sub in l ]
plt.grid(True)
plt.plot(xAxis,yAxis, color='maroon', marker='o')
plt.xlabel('No. of links')
plt.ylabel('Time taken (s)')
plt.show()

# Pages per minute
xAxis = [ 50, 100, 500, 1000, 5000]
yAxis = [ sub['visited'] / sub['elapsed_time_seconds'] for sub in l ]
plt.grid(True)
plt.plot(xAxis,yAxis, color='maroon', marker='o')
plt.xlabel('No. of links')
plt.ylabel('Pages per minute')
plt.show()

# Keywords 
xAxis = [ 50, 100, 500, 1000, 5000]
yAxis = [ sub['keywords'] for sub in l ]
plt.grid(True)
plt.plot(xAxis,yAxis, color='maroon', marker='o')
plt.xlabel('No. of links')
plt.ylabel('Keywords')
plt.show()

# Downloaded bytes
xAxis = [ 50, 100, 500, 1000, 5000]
yAxis = [ sub['downloader/response_bytes'] for sub in l ]
plt.grid(True)
plt.plot(xAxis,yAxis, color='maroon', marker='o')
plt.xlabel('No. of links')
plt.ylabel('Downloaded bytes (MB)')
plt.show()
