import sys
from itertools import cycle

if (len(sys.argv) < 2):
    print("usage:")
    print("")
    print("/bin/python3 kafka-partitions-json-generator.py [topic_name] [number of partition] [number of brokers (leaders)] [number of replicas]")
    print("")
    exit()

topicName = sys.argv[1]
totalPartitions = int(sys.argv[2])
totalLeaders = int(sys.argv[3])
totalReplicas = int(sys.argv[4])
brookers = list(range(1001,1001+totalLeaders))
replicas = []

for index, *ans in zip(range(totalPartitions), *[cycle(brookers)] * totalReplicas):
    replicas.append(ans)

print('{"version":1,')
print('"partitions":')
for i in range(0, totalPartitions):
    
    if (i == 0):
        print('[{"topic":"' + topicName + '","partition":' + str(i) + ',"replicas":' + str(replicas[i]) + ',"log_dirs":["any","any","any"]},')
        continue
    if (i == totalPartitions - 1):
        print('{"topic":"' + topicName + '","partition":' + str(i) + ',"replicas":' + str(replicas[i]) + ',"log_dirs":["any","any","any"]}]')
    else: 
        print('{"topic":"' + topicName + '","partition":' + str(i) + ',"replicas":' + str(replicas[i]) + ',"log_dirs":["any","any","any"]},')
print('}')
